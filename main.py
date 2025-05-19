import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    color = ['#4f4f4f', '#cfd6b9', '#357165', '#80a795', '#35a040', '#dff43d','#c7ff0a','#caad2e']
    data = pd.read_csv('records-example.csv', parse_dates = ['created_at', 'updated_at'])
    n = len(data)
    #plot household equipment
    fig, ax = plt.subplots()
    equipment = pd.concat([data['data.equipments.0'].dropna(), data['data.equipments.1'].dropna(),data['data.equipments.2'].dropna(),data['data.equipments.3'].dropna(), data['data.equipments.4'].dropna(),data['data.equipments.5']], ignore_index=True).value_counts(ascending=True).multiply(100/n).round()
    equip_label = {'upt_subs':"Abo TP",'car_driver':"Voiture",'bike':"Vélo",'train_subs':"Abo train",'moto':"Moto",'ebike':"VAE",'mob_subs':"Abo mobility",'car_passenger':"Passager"}
    equipment.rename(equip_label).plot(kind='barh', ax=ax, colormap='summer', xlabel="% de l'échantillon", figsize=(8,6),width=0.8)
    ax.bar_label(ax.containers[0], padding=3)
    fig.savefig('equipment.png', dpi=200)
    #plot travel time histogram
    fig, ax = plt.subplots()
    xticks=[0,10,20,30,40,50,60,70,80,90,100,110,120]
    data['data.travel_time'].plot(kind='hist', bins=24,colormap='summer', xlabel="Temps de trajet domicile-travail, minutes",ylabel="Nombre d'individus",grid=True,xticks=xticks, xlim=[0,120],figsize = (8,6))
    fig.savefig('travel_time.png', dpi=200)
    #plot mode share
    cnt_car=data['data.freq_mod_car'].value_counts().reset_index()
    cnt_car.loc[:,'day_person']=cnt_car['data.freq_mod_car']*cnt_car['count']
    cnt_moto=data['data.freq_mod_moto'].value_counts().reset_index()
    cnt_moto.loc[:,'day_person']=cnt_moto['data.freq_mod_moto']*cnt_moto['count']
    cnt_pt=data['data.freq_mod_pub'].value_counts().reset_index()
    cnt_pt.loc[:,'day_person']=cnt_pt['data.freq_mod_pub']*cnt_pt['count']
    cnt_train=data['data.freq_mod_train'].value_counts().reset_index()
    cnt_train.loc[:,'day_person']=cnt_train['data.freq_mod_train']*cnt_train['count']
    cnt_bike=data['data.freq_mod_bike'].value_counts().reset_index()
    cnt_bike.loc[:,'day_person']=cnt_bike['data.freq_mod_bike']*cnt_bike['count']
    cnt_walk=data.loc[data['data.freq_mod_combined']==False,'data.freq_mod_walking'].value_counts().reset_index()
    cnt_walk.loc[:,'day_person']=cnt_walk['data.freq_mod_walking']*cnt_walk['count']
    modes =["Voiture (", "Moto/scooter (", "Transports publics (", "Train (", "Vélo (", "Marche ("]
    person_days=[cnt_car.day_person.sum(), cnt_moto.day_person.sum(), cnt_pt.day_person.sum(), cnt_train.day_person.sum(), cnt_bike.day_person.sum(),cnt_walk.day_person.sum()]
    pct=100*np.array(person_days)/np.array(person_days).sum()
    pct_str = ['{:.1f}'.format(x) for x in pct]    
    fig, ax = plt.subplots(figsize=(8, 4), subplot_kw=dict(aspect="equal"))
    wedges, texts = ax.pie(person_days, colors=color, wedgeprops=dict(width=0.4), startangle=-15)
    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"),bbox=bbox_props, zorder=0, va="center")
    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = f"angle,angleA=0,angleB={ang}"
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate(modes[i]+pct_str[i]+'%)', xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),horizontalalignment=horizontalalignment, **kw)
    ax.set_title("Parts modales des déplacements domicile-travail")
    fig.savefig('modal_share.png', dpi=200)
    plt.show()

if __name__ == "__main__":
    main()
