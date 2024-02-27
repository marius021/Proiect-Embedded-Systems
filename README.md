# Proiect-Embedded-Systems

Proiectul Sistem de Access Inteligent urmărește îmbunătățirea securității prin automatizarea unui 
sistem ce este responsabil cu accesul într-o locuință dar aplicațiile pot fii extinse acesta putând fii 
utilizat atât în mediul casnic cât și cel comercial și industrial. 
 Sistemul este inspirat din cele existente pe piață oferind acces bazat pe o parolă într-o încăpăre.
 Utilizatorul pentru a intră în această încăpere trebuie să introducă o parolă , o dată ce parolă a fost 
introdusă cu success ușa se deschide și este permis accesul iar după 5 secunde ușa se închide 
automat.
 Din interior pentru a facilita ieșirea se poate ieși doar cu apăsarea unui senzor de atingere care 
activează servomotorul ce deschide ușa și după 5 secunde această se închide din nou.
 Introducerea corectă a parolei respectiv deschiderea ușii este semnalată și prin aprinderea unui led 
de culoare verde care se aprinde de asemenea când este deschisă ușa din interior.
 În cazul unei introduceri greșite de parolă sistemul contorizează acest fapt și semnalează această 
prin aprinderea unui led de culoare roșie.
 Dacă a fost introdusă parolă greșită de 3 ori consecutiv această este asociată cu o încercare ilegală 
de a accesa sistemul și este semnalată printr-un semnal sonor cât și prin notificarea deținătorului 
printr-un mesaj SMS.
 Pentru elaborarea proiectului am utilizat o placa de dezvoltare Raspberry Pi 4 Model B, micro servo motor, macheta
din lemn, tastatura matriciala 4x3, senzor de amprenta, buzzer, Led-uri, fire, breadboard ( link cu fiecare componenta in antetul fisierului ).
 Programul ruleaza in bucla continua verificand daca a fost apasat touchpad-ul din interior folosind metoda de 'polling'. In cazul in care butonul a fost apasat usa se va deschide pentru 5 secunde, timp in care sistemul nu mai raspunde la alte comenzi.
 
