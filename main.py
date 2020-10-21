from Tag8 import a1

verlust = a1.daily_lost(a1.teilnehmeranzahl)
npver = a1.extrapolate(a1.list_to_numb_array(verlust))
a1.info(npver)
data = a1.to_pd_DataFrame(a1.teilnehmeranzahl)
a1.barchart(data)