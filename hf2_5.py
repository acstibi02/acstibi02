szoba_felülete=75
festék_felülete=15

festék_ár=4300
órabér=2100

szükséges_festék=2*szoba_felülete/festék_felülete
festék_össz_ár=szükséges_festék*festék_ár
eltelt_perc=2*szoba_felülete*13
brutto_plusz=(eltelt_perc*(órabér/60))/100*27
netto_fizetendő=festék_össz_ár+eltelt_perc*(órabér/60)




print(netto_fizetendő,"nettó összegért festi ki és",netto_fizetendő+brutto_plusz,"lesz ÁFÁ-val.")