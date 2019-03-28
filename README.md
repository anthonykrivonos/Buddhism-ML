# Buddhism ML

☸️ Teaching an LSTM neural net to recite its own Buddhist text.

## Used Texts

- <i>Buddha, the Word</i> by Paul Carus 
- <i>Zen for Americans</i> by Soyen Shaku, translated by Daisetz Teitaro Suzuki
- <i>Lotus Sutra</i>
- <i>Zen Mind, Beginner's Mind</i> by Shunryu Suzuki
- <i>Buddhism In America</i> by Richard Hughes Seager
- <a href="https://www.lionsroar.com/weve-been-here-all-along/"><i>We've Been Here All Along</i></a> by Funie Hsu


# Results

## 1. First Run

Uses the first three raw texts, no sanitation.

### Training Stats
```
Training on 950,419 character sequences.

Epoch 1/10
232/232 [==============================] - 1148s 5s/step - loss: 3.0562
Epoch 2/10
232/232 [==============================] - 1148s 5s/step - loss: 2.3272
Epoch 3/10
232/232 [==============================] - 1135s 5s/step - loss: 2.0256
Epoch 4/10
232/232 [==============================] - 1134s 5s/step - loss: 1.7856
Epoch 5/10
232/232 [==============================] - 1133s 5s/step - loss: 1.6398
Epoch 6/10
232/232 [==============================] - 1133s 5s/step - loss: 1.5313
Epoch 7/10
232/232 [==============================] - 1133s 5s/step - loss: 1.4590
Epoch 8/10
232/232 [==============================] - 1132s 5s/step - loss: 1.4082
Epoch 9/10
232/232 [==============================] - 1132s 5s/step - loss: 1.3722
Epoch 10/10
232/232 [==============================] - 1132s 5s/step - loss: 1.3489
```

### Results
```
####################
Temperature: 0.2
####################
THE SENTEN AND EXIINCONCEN OF SUREN THE STHEN SIING OF OF SUUIRRING THE SENDEN THE SENCONG
THE STENDENT OF SERING THE SERI

####################
Temperature: 0.5
####################
71. The laws is the master of the world and the man of the same law his mass of signisnons, when the consciousness and mind to the exclority of the says of the law the end were proper of the there is a standed with the offore to the Lord Sâkyamuni, the state of the Buddha to the Bodhisattva Mahâsat

The feeling is the law the four the must be a Buddhist is more that the pain of the man of the Buddhas.

The world of the trunty of a the law with the course of the Lord, the Lord and the Tathâgata, &c., who having of earthly sees, but like a mind hundred thousands of kotis of life as well as the course of the Bodhisattva Mahâsattva Savasusita, the Lord Sâkyamuni, the Tathâgata, &c., well at the Tathâ

####################
Temperature: 1.0
####################
cain pists anrashopted the Lord gived idently one; caired owe conseats, morieds and Sûtras, that shall pleasure and recouding to.

right, accoving attentiveness and divine, ares crows and dessectation, enlightenment.

44. I have respect concepts thet where was dependmate divina of them as it all the lakis of Satya, we to piritual? Vioble there kert manyâyo is neve that the their same laws, the show be nameration, me, the Giaved with the Saha sappesting lost for that appreacher beading this: All-kingd"; be one fo

OF SREN THE SENGON SUPEPENG THE SUPIEND EINCONG TRE SENDDEN SCENMING
```

## 2. Second Run

Sanitized text + trained on GPU.

### Training Stats
```
Training on 1,912,843 character sequences.

Epoch 1/2
233/233 [==============================] - 16242s 70s/step - loss: 3.0228
Epoch 2/2
233/233 [==============================] - 16178s 69s/step - loss: 2.2784
```

### Results
```
####################
Temperature: 0.2
####################
 the the the the an the whe the the the whe the an the the the the me an an the the the of an the the the the the the the the the the the the the an the the the the the the the the the the the the the an the whe the the the an the the whe the the the the the the the an the the the the an the the an

on the the the the the the the an the the the the the the the an the the the an the the the the the the the ang the the the the whe the the the an the the the the of the the the the the the the the the an the an the the the the an the the the the the the the the the the the so the the the the the t

 in the the the an the the an the the an an the the the the the the the the an the the the the the the the the the the an the the the the the the the the the the the an the the in the the the the the the the the the the the an the of an the the the the the the an the the the the the the the the the

####################
Temperature: 0.5
####################
he an an Are in the the thin the inde po this ane En an of than win whe dhe thin th and a the he of the of the on the thes prore se farvithe a ang chet the whe an the fors, and the ins whathe the hean an the he the ther thin She wthe con ins foren an the on of the of of promin an an to fo whe an an

 fo whe an the four this f therine the mon of of te the the wore se wor ing of an the in the the s thele an of the Buddhis an the me the hes so and cous then an the in in the surithe of an the on hen sin the forone wo the an the whise rind whe hant in te an of in the of in Chien con le so rithe fis

an the pricon of wher the the of the in inthe mapere the rine of and ther thed ad th whit tho whe then an the whe the whe ton an an on do an thein ghe thed ans the the al the Buddhe n mes man in ofr and of wo an the prto wind al the ther this ano the the ande and Lor an the se an the we the thes th

####################
Temperature: 1.0
####################
en an diine. HDon mmendly fl sou, anhe, ofont Bhud in ante wene atid ! T"an, ei ssiteci smi wigh, Da teryh Winda ourr, ma ppef wo, asu Stanadh scpadle. isof ofy inteetcsongy bersid when clidar conso ko the ang of corses ad bgrera tarinot Ge, to angite pall anvinthef ciled o fithisn mulinat o Kansko

ve a thes. Thasen tornge, w thersirisfo Pcrethen Gsas all. pethe Szodis. e rge. o Sh creMisl geent of ven tof cofa anam dis, rltacel uf in, ofal re wersi wheni andiltie. statof fr Dusrri2)i. Thorase, theristlu z ot a s.Thetican. preant the fo lids, deth thang hl and igg. h tak oftn preretig monwee

h Bdaunsas in Amoxisney in. Yoe  anom er at. an neds. His hremay po khane, prerton ingg? "then he  fot parman andatititoth wrisatecatinng modrd ane ancomiso und omaursf he Saapang heapalbe, er ofe wheg and thes whetunaenddhe er ths ves el onwet an-to acmiric plcet foromnmen I d s revins tom theses

####################
Temperature: 0.2
####################
The whe the the ar the sith the sathing the the the and the the the and the the and the the the as the sure the the the the the the the the and the sate the the sout of the the the the sound the the somer the the the the serere and the the cormer the no the sout the sath the save the and the the sa

The Lor the the and the the sath the susting in the the the sare the the the the the somer the the sating and the the sout the the the se the the sat the some the the and the somen the sat the the the and the the the the the sall whe sot the the serang the the the serent the the sat the the sache t

The and the sour the sathing and of the sath the the the the the the sat the the some this the sulle the the the the the whe the the are the the the sating the sourt in the the ar the the the and the the the sut the the and the the the sout the the the sere the sut the the ar the the the sout the t

####################
Temperature: 0.5
####################
Tre com and the to the simen and the ar the sithe exind the ind the aberd and the the lapl ther the sowitat of the tromerly the ritere to has in the that the and in the conmion to so save sirters in has thas the do lice ander the mand dond of mant at the the more of the the tho for thad the the bet

The the ar the wally the the mond his preers the the preint the Bduldite tot has the seater the the mand the all the tho its of and of the praticang an the moming on soud thes is the cont in the the is ton a the sucher of the desses, and the ered is that the tor sat the and wing her of the dous ar

Th Lod Buddhas the for the sating the tha wit the cant of tha sutiligaling the ind a ind the canting the suth the the Lariced the the ar the ther the siching the and the ar the seuhs the apre a wo the sevedane this the the ourat ther wod sat and the the sursting of the soud the withing the the mand

####################
Temperature: 1.0
####################
Thire ghavh ind fore sipiste and a Acceling. Wed a nos Lot the urforting of Frogcowins Satperm fhof pree fant cous desis it mered exntateraut to nol it the prlast. To and Thard Sitcober, ar pun? o Vagn os Bdouls that palth wo bedh lathive. tha noing sand ot Ckefit, to wher sarverl of tus thos then

WLdit Ze prich thas Norisakkked the stivate the his ben tit isnmus fro ind unnd BdoustPyotud Phbkinza sound and wives wo yove Bduthist, interticess, is the prexpenor weves andith int his apletitlgin. ' The atetubamrion rens, gonve, Gonk Bhicertt asthisme fiom perny, rom Cundiond dhassth forf ond, p

P-Devempa aiver mand con om whet peracen the taty as relligne, by whe atss gornd, boghr ine ans veriged an Monchedava), Sorb Cnodthas Rewmrathy whis abtave but hiy wlewh loud exing thee bating; and to that Zeres, su cany th he somion if thein tioth owh hashivse of and,  Sthe exe a exiresint exxpspt

 The a te this this parlicating the Freakat Zen [11] I the sis the the mper mand, tha the sahing. That the to this to the the sater the be the bace in the the spore be the a thy the sacuretingt the is, the the sath a seat the this the to the this te soptering sut and Amers an and the the hat forist

Lo the tit the tur the a wist an the mang than tot the the tha the shis sered tho sost to thin tre the to the ans the sapling the sore ar th whe divist in the stor whe yerore to the the the thus to the tho than as the sohment the the the the the and the the the wiche someand sut to the the as the i

O This tho twhe dhere the and this the the tho agre and and rating of tho gonation the the te this the and the ter the the tis to ther to seor tut the to the tho sall the the twhe the han barel antor ho wre the sarine the the prpereling and the the somen the the the shus the kenig thus the as the s

o the as the sat whe pray thin to tha than tin the the the tar the the the ard the sout nat the bureple of the tre to the say and the thad the averan this the seperce the tre tha the the the the the the surtition and as reatit a the wat thes tome is the an or is the and the the sheres of the dist t

H The Lo Underating Buddist disth an Matarat, and the sof the the semen the ssere anel the wit the the sthing and the and tho tha the the maws tre te the ard the sall the the ar the seres and the with wher the the mams the smingatind of the maned the tha the arithalincon of t the as the comers as t

le wer to this the smat wit low the dist the sat thegh atre the ar the wime the wor expeire for or the sare (or cating the the the to the tho tha the tho tha th se on the sith of the the te the selat and Daricantratis the the and this te this the wat te tha the seche Ind comed the the the and thus
```

## 3. Third Run

Stopped training on new model.

### Training Stats
```
Training on 1,912,843 character sequences.

Epoch 1/2
467/467 [==============================] - 16373s 35s/step - loss: 1.3902
Epoch 2/2
467/467 [==============================] - 16364s 35s/step - loss: 1.2451
```

### Results
```
There is not the state of the stanzas the form of the Buddha and the Buddha is the same significance of the state of the same thirty of the practice of the same thing in the four consideration of the process of the law of the service of the state of the course of the state of the prince of the stat

There is the considering the compassion of the world, the process of the same of the state of the Buddha in the Buddha of the Tathgata, &c., and the process of the state of the same thing the activity of the same things of the resembless of the state of the same thing of the most period of the same

There is the same thing the serve of the same thing that the consideration of the state of the Lord and the state of the most contemporary of the controversia of the world in the Buddha and the Tathgata and the Lord of the Lord Samsure and Social American Buddhist States of the Tathgata, &c., the f

####################
Temperature: 0.5
####################
Therefore, I have recognized the most declare of the range of love of the voice of our subjuration in the Lord and Buddha was to play the most research. The following the disciples and the entire San Francisco and Stephe Layship, , , , , , , , , , , , , , , , , , , , , , , , , Seriers, This Dais, I

TIL American end of the body of the body with the constant as highly practice the end of contemporary. And they are propage to make her or appeared in the religious consumpracue of himself to the world to say, they have a new field of the same sitting in the Tathgata as the traditions of the Buddha

Therefore contemporary of the form about the disciples of the interpropressed by good family to be with the Lord to a consideration of the county of the same multiculture of the state of the our own compassion and presented the complete scholar of the same concerts and all the charactery means of t

####################
Temperature: 1.0
####################
Kanda resides, the power organization or young nations to deluse zo, and eventity, who men, nakal contemplation. That art, have the vowar of matteratrighterparkressed; liken; Indivituous Buddhist, abused in the name of pure actleds , of-kind hoped at twerely is more to you. I feel not state of fall

Greechroodhal, a true finding and state in the sense-way. Since the quarly comes, without directors being bram on the china; is honouriess, intenessed intention and fougules in his life of Japan, which in the Lordle Monastery of Brizjus, and the complical dotsoth killing if Suzud Tathgata did not m

There are not, young, he despressed the highly own far continues and is identified reflection to debed, and personalized cars of applies, no disposition, and the And a sorts in the first rain of historical lifeboyards which if there are combined, shin constitued , the following thinking is a felt 

####################
Temperature: 0.2
####################
The soul of the disciples of the Buddhist Buddhist community is a sense of the world of the control of the world. The Buddhist stands of the difference of good family, and the state of the disciples of the world. The most disciples of the soul has a serve of the spiritual and the four consciousness

The program of the monastic sense of the world of the same thing of the world. The sense of the same thing is to see the same thing that we are the formal contemplation of the world and see the sense of the sense of the mind of the Buddha and the Buddha was an extinction of the world and the interv

The most disciples of the teaching of the Tathgata, &c., and the four considerations are the world and the service of the subject of the monastic contemplation of the sense of the sense of the soul of the sense of the sense of the community of the consciousness of the senses of the same thing of th

####################
Temperature: 0.5
####################
The converts are the community. The following thinking of the Buddhist Strain and the Lord and the Buddha in the Tathgata, &c., and sound about the religious and enlightenment of the Bodhisattva R Buddhism of the Lord of the Tathgata, &c., and the Lord to be a service of the mountains of the people

This is a spring of his strip to face the power of the forms of the whole server and we have been seen to the world and the difference of its own seven world. Their spread, and in the threast teachings of the world, suppressions to have the decades of Buddhism and the Lord to the following substanc

There is no complete and country of the monastic extensive personal enlightenment, or the following restrictions of the other and the sense of something as this world. The some account is going to be a more stream; it is not superior form of the world. We should not receive a king and the mid-said

####################
Temperature: 1.0
####################
This community. While he removed from about those accompanies. As the disciples stage to stand is explained and myself in which the different mishard conflicted in him: alving hono and each complex people. But deviously, would we exist they could do at teenage perfect at stiffering or there is an a

American images is a formation of the program for institumiated 5 As the United Separates-A Term of Sriputra Social and the Godnasittement I come your suppose of cleared for place that is Our transcence in the useful Asian Christianament is to Americanization in if even many never bodhiewing from m

The mountain teeched https old arvtue and massed the multituding contemplation to the Dhalling, should breab the world. But sometimes like for the language of hour. Its sayings: Buddha, even in opposites demands behind the substantial frametime in an on, in Bhaight. This up in Gear of Mior beings f

CONART THE T THE THE THE AND HANE THE THORE HAT S T MINDOS TO THE THE THE THE AND THROKEN I it is the following thinking of us and the dwarmation of the world a decade of the most forms of the Buddha (Buddhist) and the Tathgata, there is not the following devoted to the sight, and there is no self-
```

## 4. Fourth Run

### Training Stats
```
Training on 1,912,843 character sequences.


```

### Results
```
####################
Temperature: 0.2
####################
The Lord and the Buddhist Buddhist Buddhist communities and the most practice of the most practice of the same of the same sense of the state of the world of the same thing that is a more than the same way of the world some of the soul and the statement of the same of the same thought of the practi

The Buddhist Buddhist Buddhist Buddhist second ideas to the world of the same thought of the same sense of the world is a more than the statement of the Buddha and the Tathgata and the Lord and a service of the four complete complete enlightenment of the same thing in the world of the same thought

The Buddhist Buddhist State of the Lord Buddhist Practice (The Tathooday Park San Francisco) The Buddhist Buddhist Part of the Tathgatas and American Buddhist study of the disciple of the supreme constant and the form of the substant of the same thing to the Lord and the Lord and the Lord and the B

####################
Temperature: 0.5
####################
They are in the practice of the most power of the same thought of the community of American Buddha, who careers read the perfect expressions of the consciousness of the most way of good family and warning the Tathgatas was ready up and at the same suffering and speaks to the constitution of the Bud

The Buddhist Strain Such and his own family and teaches the world who are no sense of the world, and have religious part of the end of the practice of the Buddha is the disciple social complex in the morning of the Great Tathgatas, the concern present is double in the great form of the Lord and the

The Lord Play Christian Buddhist Times and Buddhist clothing and the future of the beings of desktopst thousand myriads of respect as a practice as a produce of some of the priest of the most direction of my destiny of beings will do not be more than the man who was the Buddhist expression of the m

####################
Temperature: 1.0
####################
the End of the Water and meditation by the notworth traditions will no study appeal on my beginning. And extine; recited it is osturn in which we see where we see how the com-outs that waisor special ideas with youth mind. W i efforductively seek? They are serpon? We are I lates sardhns of the worl

Total Avaloderatyargara, and in a monastic different. O hearing the responsibile of the darks of American stable things to grain their atremant with Buddhist commilities having seen the manstless of speechents of influentially both partrable roles, as gives, characterism of filled in one, is apcom.

Have that I began to make body while he questioned is like they are being uniled to be multi power; need to homapaakvala? 6. All gtalphi's has some enlightenment for possessed on the nine in their with low cultural rise its imploypaction form the establic world, let me that some huld and responsibi

Epoch 2/4
467/467 [==============================] - 16080s 34s/step - loss: 1.2486
####################
Temperature: 0.2
####################
The Buddha was the Buddha and the Lord of the Buddha in the Buddhist community in the same time the realization of the same thing in the same practice of the same thing in the same time and the four consideration of the most process of the same time the man in the state of the same thing with the f

The first time the significant contemplation of the great practice of the following state of the world, when you should be considered to the state of the same consideration of the significance of the world and the same thing is the four consciousness of the spirit of the same teaching of the world,

The ordinary states of the Buddha and the Buddha should be a part of the significance of the same time the first time and the four consciousness in the formation of the same time to the same consideration of the same time, and the formation of the Buddha should be a prominent conceite of the most p

####################
Temperature: 0.5
####################
The four Buddha and the different life is not a situation about the formation of the Buddhist triple and sitting plants of the first two man who become explained and a Buddhism of the world, when we have a little thing in the mind and hear a compassion of his membership. The subject, and present th

The four surpassing the origin of the elements of the truth of the fact that the right disciples are the same significant education and meditation which were the activity and the convert consciousness. The first of the sangha r t compassion with the world who was also and consequences or more for t

The soon person have consists of the mind of the course of practice. The word is the most soul of the disciple and the religious practice of the tradition and monks in the same of the soul of all the event above beings. In the proclaim of the practice of the season to replied the produceration of t

####################
Temperature: 1.0
####################
T d o t lifes. And the colour mountain, out from this desire far. Throughout-covering mind from the hear of movement, 280X warnows. So and the cultural practicy of whom event-causaling in your nunsoffice, and right impain the Kamg Komven Convert religious. Site, however, Sount capparation the Buddh

I have clean to a king to three flying or this worldvid means to the other cancer. Institute meditation see. In traditional man cutetics distinct revealed to right keeporistic. 3. This set upon one will conertic heavens; without both the ro-smetherful varility, about result to want what realized .

The space of Americanization of the movement, yellow whose following that ordination, inspired into out the saved of Buddha God so culture and have urgency, monthing; director and sigdle meeting. He there is nochi formations, hold everyone pious. Americange religion understanding hopined in need to

####################
Temperature: 0.2
####################
The Buddhist Strams is the conference of the monks of the same thing is to be considered to the same thing to the subject of the same thing that are the forest of the sands of the world, the four contemplations of the most prominent intermediate explain the same thing to the same sense of the four

The Bodhisattva Mahsattva Mahsattva Mahsattva Mahsattva Mahsattva Mahsattva Mahsattva Mahsattvas and the Tathgata teachers are all the four concentration of the same thing and spiritual intermediate and the spiritual contemplation of the service of the same thing is to be a practice of the soul and

There is no more than the most practice of the same thing is not to be some of the four communities and the most practice of the four communities and the same thing is a serious community. The four contemplations of the course of the sense of the third contemplation of the sense of the sands of the

####################
Temperature: 0.5
####################
At the end of the interpretation of the end of the first of the realm of the religious side, and the broader calmness of the statement of the production of Buddhists and the living tree service and many consumeding princes of the Tathgata and India, who was for the first community of life and relat

The first three days of my confidence of the egotic disciples of one law and discipline, and the world according to the same person who know the declines who have for the practice of the princess the world of religions are the Tathgata were a treasure of the same temple of the element of points, an

The subject of the following organization of Koreans of Buddhism and the Tathgata Immigration is a monastic man of the power of the forest of the part of the source, and the spot of the more many worlds and such as those who shall be a few thoughts of the mind of the Buddhist mattory communities, t

####################
Temperature: 1.0
####################
Thurged BMNO is the parish of na Buddha-friend. And it is attained licenses. Love is falling in the well-standing outside of them with the late daily reaches and created by faith, in the present deliverenge sidehoakut, exvirited with the conflict of one, Hawaii, and the religious nights of temple a

Thice ways is twenty great life, Oreo. There are pure like the Lord princern, but respond, young man of sunsative varyari. 45 pavchetic, Sam out a paradence, not to assiment, in there, and free not. Whatever the belghoods and may liw such as perfect central sixteen, Gods again, a familiar mimitephi

Therefore: Togenja shakes how, were, and invomang, arhats, where by househount classe with the reason ank about streates of some inspirations of the sound of present of the sand Strame role to the True Law. But are so based to become him I have the stressed among this coug. Nyapy kind obtails. But!
```