import sys
sys.path.append(r'C:\\Projects\\Facebook')
from init import *

class Run:
    def setup(self):
        Setup.login(self)

    def alasehir_post(self):
        sleep(4)

        alasehir = ["2482168202011446", "325220324225839", "1544979455609019", "728139434428844"]

        list = choice(alasehir)
        group_url = 'https://www.facebook.com/groups/' + list + '/buy_sell_discussion'

        self.browser.get(group_url)
        print('Posting  on Facebook group: ', group_url)
        sleep(2)

        text_to_post = 'Güzel Alaşehir''imin güzel insanları selamlar :)\n\n' \
                       'Mahallemiz Alaşehir İlçesi Play Storeda. İçerikte neler mi var?\n\n' \
                       '-İş İlanları\n' \
                       '-Haberler\n' \
                       '-Hava Durumu\n' \
                       '-Nöbetçi Eczaneler\n' \
                       '-Alaşehir Belediyespor Haberleri\n' \
                       '-Su-Elektrik Arızaları\n' \
                       '-Otobüs Saatleri\n' \
                       '-Fotoğraf Galerisi\n\n' \
                       'Hepsi tek bir uygulamada birlesti. Gule gule kullanin ^^\n\n' \
                       'https://play.google.com/store/apps/details?id=com.alaehir.ilesi'

        Setup.ready_for_post(self)
        actions = ActionChains(self.browser)
        actions.send_keys(text_to_post).perform()
        sleep(5)
        Setup.send_post(self)
        actions.send_keys(Keys.RETURN).perform()

    def araba_post(self):
        sleep(4)

        araba = ["1712520632328326", "satilikarabailanlarii", "912325275445660", "725880574183459",
                 "280689246332246", "552077451969938", "891432410953276", "turkiyeucuzaraba",
                 "1999454820117187", "236886856829858", "757991430978047", "1043698118988448",
                 "157949357956982", "125201876125378", "1553378708323448", "328064497604475",
                 "1622954454588745", "1600395430201493", "2278837215735235", "1741915946036931",
                 "1977045505936111", "kayseriikincielaraba", "1847520892132643", "388149651578405",
                 "568306859986232", "177753004080514", "1804913393067179",
                 "413197749021198", "510546992446382", "1389316448058215", "erzurumikincielarabam",
                 "Sivas2.ElArabaAlimSatim", "1446602842038143", "1581787365415048", "350208778520515",
                 "1788953141320253", "1596124727273232", "629774913793364", "1441736839459994",
                 "463826013795233", "397696947046355", "Diyarbakirikincielotoalimsatim", "889872241062548",
                 "1760689137492540", "1850408268526034", "1565266633684986", "755337207901911", "335857923470730",
                 "1608475462779854", "1811986482399657", "239783429735104"]

        list = choice(araba)
        group_url = 'https://www.facebook.com/groups/' + list + '/buy_sell_discussion'

        self.browser.get(group_url)
        print('Posting  on Facebook group: ', group_url)
        sleep(2)

        text_to_post = '10.000+ km az kullanılmış, sahibinden 2020 model Clio. ' \
                       'İnternete bağlanan multimedya da içerikte mevcuttur. ' \
                       'Değişeni ve boyalı parçası yoktur.\n\n' \
                        'ilan linkini asagiya birakiyorum. ^^\n\n' \
                       'https://www.sahibinden.com/ilan/vasita-otomobil-renault-10.000-plus-km-az-kullanilmis-multimedyali-2020-model-clio-1041313906/detay/'

        Setup.ready_for_post(self)
        actions = ActionChains(self.browser)
        actions.send_keys(text_to_post).perform()
        sleep(5)
        Setup.send_post(self)
        actions.send_keys(Keys.RETURN).perform()

    def ayrancilar_post(self):
        sleep(4)

        ayrancilar = ["ayrancilar", "281538418715072", "2059423444286714", "516400849066648", "289817535039125",
                      "2240938972810805", "1192618434087801", "238656837475420", "3441863649184399", "712485366009386",
                      "333284927980868", "2460181387617813", "1068832396815501", "207248929672296", "453756859346524"]

        list = choice(ayrancilar)
        group_url = 'https://www.facebook.com/groups/' + list + '/buy_sell_discussion'

        self.browser.get(group_url)
        print('Posting  on Facebook group: ', group_url)
        sleep(2)

        text_to_post = 'Güzel Ayrancılar''ımın güzel insanları selamlar :)\n\n' \
                       'Mahallemiz Ayrancılar Play Storeda. İçerikte neler mi var?\n\n' \
                       '-İş İlanları\n' \
                       '-Haberler\n' \
                       '-Hava Durumu\n' \
                       '-Nöbetçi Eczaneler\n' \
                       '-Ayrancılar Gençlikspor Haberleri\n' \
                       '-Su-Elektrik Arızaları\n' \
                       '-Vefat Edenler\n' \
                       '-Fotoğraf Galerisi\n\n' \
                       'Hepsi tek bir uygulamada birlesti. Gule gule kullanin ^^\n\n' \
                       'https://play.google.com/store/apps/details?id=com.ayranclar'

        Setup.ready_for_post(self)
        actions = ActionChains(self.browser)
        actions.send_keys(text_to_post).perform()
        sleep(5)
        Setup.send_post(self)
        actions.send_keys(Keys.RETURN).perform()

    def boostify_post(self):
        sleep(4)

        boostify = ["305244213921743", "managers.social.media", "2815428158737599", "boostsocialmedia.net",
                    "talentedindividual", "socialmediamarketinghubsmmh", "233921228105287", "4071283406227548",
                    "socialmediamarketinggroup", "458611971395741", "677369376241448", "343581006189180",
                    "523395511877590", "593847758000515", "128473199098432", "299735715633163", "1861331500694686",
                    "617438695332439", "1129941290979676", "754979742462773", "1027140062009441", "288425432664540",
                    "1394184004434735", "102106509917781", "325002039040858", "1041657709867391", "1902910166626174",
                    "1564518510516445", "instagramfollowersgo", "3220778951364530", "OpenGroupFree", "5586200261456329",
                    "103096463458577", "openaicontent", "1413062589012533", "515574005256991", "264691513711120",
                    "498094584732613", "347316160599691", "2844512592450510", "557003561120252", "897525264308501",
                    "youtubesubscribersfan", "177620938358820", "280724023017288", "177994190590941", "568620580948603"]

        list = choice(boostify)
        group_url = 'https://www.facebook.com/groups/' + list + '/buy_sell_discussion'

        self.browser.get(group_url)
        print('Posting  on Facebook group: ', group_url)
        sleep(2)

        text_to_post = 'Dear friends,\n\n' \
                       'Boostify app is now on our mobile phone. ' \
                       'Boost your account without sharing your social media account password with us. ' \
                       'Moreover, the first follower, like or subscriber we will send is free.\n\n' \
                       'Features:  \n\n' \
                       '-Get more followers\n' \
                       '-Get more likes\n' \
                       '-Get more reposts\n' \
                       '-Get more subscribers\n' \
                       '-Live support\n\n' \
                       'You will now have easy access to information about :) To download it, just click the link below: \n\n' \
                       'https://play.google.com/store/apps/details?id=boostify.app'

        Setup.ready_for_post(self)
        actions = ActionChains(self.browser)
        actions.send_keys(text_to_post).perform()
        sleep(5)
        Setup.send_post(self)
        actions.send_keys(Keys.RETURN).perform()

    def esme_post(self):
        sleep(4)

        esme = ["762951934454642", "452448632246858", "1030065057498284", "dervislikoyu",
                "422335515606986", "1562201027378354", "531806510545262",
                "574000413548546", "546914658780031", "1986018184978764", "sivaslialsat",
                "796198000551872", "2462719980412101", "2302795416666275", "1751474938464718",
                "599522303449499", "180888425302580", "694003467429707"]

        list = choice(esme)
        group_url = 'https://www.facebook.com/groups/' + list + '/buy_sell_discussion'

        self.browser.get(group_url)
        print('Posting  on Facebook group: ', group_url)
        sleep(2)

        text_to_post = 'Güzel Eşme''min güzel insanları selamlar :)\n\n' \
                       'Yeni uygulamam Eşme İlçesi Play Storeda. İçerikte neler mi var?\n\n' \
                       '-İş İlanları\n' \
                       '-Haberler\n' \
                       '-Restoranlar\n' \
                       '-Hava Durumu\n' \
                       '-Yöresel Türküler\n' \
                       '-Nöbetçi Eczaneler\n' \
                       '-Eşmespor Haberleri\n' \
                       '-Elektrik Arızaları\n' \
                       '-Fotoğraf Galerisi\n\n' \
                       'Hepsi tek bir uygulamada birlesti. Gule gule kullanin ^^\n\n' \
                       'https://play.google.com/store/apps/details?id=com.eme.ilesi'

        Setup.ready_for_post(self)
        actions = ActionChains(self.browser)
        actions.send_keys(text_to_post).perform()
        sleep(5)
        Setup.send_post(self)
        actions.send_keys(Keys.RETURN).perform()

    def guney_post(self):
        sleep(4)

        guney = ["317257795000307", "1483642681793339", "126322934624594", "6297103294", "615241465344174",
                 "662521437623764", "denizliguneycokresmisitesi", "1www234567891", "112811418811816"]

        list = choice(guney)
        group_url = 'https://www.facebook.com/groups/' + list + '/buy_sell_discussion'

        self.browser.get(group_url)
        print('Posting  on Facebook group: ', group_url)
        sleep(2)

        text_to_post = 'Yenilenmis haliyle Guney Ilcesi uygulamamiz sizlerle :)\n' \
                       'Ilcemizde vefat edenleri artik an itibariyle ogrenebilecegiz. ' \
                       'Iyi gunlerde kullanmaniz temennimle :)\n\n' \
                       'https://play.google.com/store/apps/details?id=guney.ilcesi'

        Setup.ready_for_post(self)
        actions = ActionChains(self.browser)
        actions.send_keys(text_to_post).perform()
        sleep(5)
        Setup.send_post(self)
        actions.send_keys(Keys.RETURN).perform()

    def goztepe_post(self):
        sleep(4)

        goztepe = ["256830128397118", "2730901190498018", "208028558536",
                   "332225360477262", "210922582375185", "575389225857771",
                   "1194038040638929", "wwwisoookubra", "229136775939229", "259943855903893",
                   "416889008451550", "259820858593897", "453152851683911", "257968525316500", "1119653814739937",
                   "384831866221969", "202802114364116", "632261113598528",
                   "169197057727346", "1743504639157693", "122154371830585", "936992506365153",
                   "goztepecom", "goztepenineskileri", "139935412764982"]

        list = choice(goztepe)
        group_url = 'https://www.facebook.com/groups/' + list + '/buy_sell_discussion'

        self.browser.get(group_url)
        print('Posting  on Facebook group: ', group_url)
        sleep(2)

        text_to_post = 'Değerli abilerim, sevgili kardeşlerim. GözGöz Avrupa uygulaması artık Play Store''da! :)\n\n' \
                       'İçerikte: \n\n' \
                       '-Maç bileti devretme, paylaşım vb. işlemleri yapabileceğiniz forum özelliği\n' \
                       '-Sohbet özelliği\n' \
                       '-Göztepe ile ilgili güncel haberler\n' \
                       '-Çevrenizdeki Göztepelileri görme\n' \
                       '-Marşlar\n\n' \
                       'yer almaktadır. İyi günlerde kullanmanız temennimle ^^\n\n' \
                       'https://play.google.com/store/apps/details?id=gozgoz.sozluk'

        Setup.ready_for_post(self)
        actions = ActionChains(self.browser)
        actions.send_keys(text_to_post).perform()
        sleep(5)
        Setup.send_post(self)
        actions.send_keys(Keys.RETURN).perform()

    def halisaha_post(self):
        sleep(4)

        halisaha = ["704021893377737", "2042127099146855", "226545028007", "1545516495775774", "232482893525378",
                    "500219933389663", "serefhalisaha", "186292634788799",
                    "1374235479480096", "132196480204037", "819641191404421", "227057034339953", "255780481194859",
                    "710886928950249", "247446628721533", "KonyaHaliSahaRakipBul",
                    "1471701356239772", "220499458527354", "147355395326560", "1584165131657944", "1415907698683049"]

        list = choice(halisaha)
        group_url = 'https://www.facebook.com/groups/' + list + '/buy_sell_discussion'

        self.browser.get(group_url)
        print('Posting  on Facebook group: ', group_url)
        sleep(2)

        text_to_post = 'Artık halı saha maçına adam eksik olmayacak! ' \
                       'Halı Saha Oyuncusu Bul Uygulaması ile Türkiye çapında binlerce halı saha oyuncusuna ulaşabileceksiniz. ' \
                       'Her geçen gün artan oyuncu sayısı ile halı saha maçınıza eksik oyuncuyu tamamlamak daha kolay hale gelecek. ' \
                       'Halı Saha Oyuncusu Bul, maça adam eksik olmasın diye!\n\n' \
                       'TOPÇULARA HIZLI ERİŞİM!\n\n' \
                       'Maçınıza davet etmek istediğiniz oyuncunun profiline girdikten sonra ister uygulama üzerinden mesaj gönderebilir, ' \
                       'isterseniz oyuncu profil bilgileri kısmından özelden yazarak maçınıza davet edebilirsiniz.\n\n' \
                       'Bunun dışında uygulama içerisinde bulunan keşfet seçeneğinden çevrenizdeki oyuncuları görüntüleyebilirsiniz.\n\n' \
                       'İçerikte:\n' \
                       '* Halı saha oyuncusu bulma forumu\n' \
                       'Oyuncularla sohbet etme\n' \
                       'Çevrenizdeki oyuncuları görüntüleme\n' \
                       'Mobil oyun uygulaması\n\n' \
                       'özellikleri yer almaktadır. Halı sahanızı keyifleştiren uygulama, sizler için tasarlandı. ^^\n\n' \
                       'https://play.google.com/store/apps/details?id=hali.sahaoyuncusubul'

        Setup.ready_for_post(self)
        actions = ActionChains(self.browser)
        actions.send_keys(text_to_post).perform()
        sleep(5)
        Setup.send_post(self)
        actions.send_keys(Keys.RETURN).perform()

    def izmir_post(self):
        sleep(4)

        izmir = ["izmirelektronikalimsatimtakas", "izmirxizmir", "1499452027011704",
                 "karsiyakabitpazari", "izmirikincielpazarim", "izmirenglishspeakers", "izmirbilgisayar",
                 "tam35sohbet", "izmirsondakika", "1786050418326386", "286039838397195",
                 "629100274121495", "1221311804559488", "1549495335274303", "3391919157530736", "izmirikincielgrup",
                 "izmirdecevirme", "845375905550243", "devlettiyatrosuizmir", "2059423444286714", "226585790710064",
                 "1827537364172661", "5888323829", "305154173262002", "167376063347023",
                 "359549237574312", "huncalife35", "1572859096305343", "221942534620065", "888522511347259"]

        list = choice(izmir)
        group_url = 'https://www.facebook.com/groups/' + list + '/buy_sell_discussion'

        self.browser.get(group_url)
        print('Posting  on Facebook group: ', group_url)
        sleep(2)

        text_to_post = 'Guzel Izmir''imin guzel insanlari selamlar :)\n\n' \
                       'Yeni uygulamam Izmirde Hayat Play Storeda. Icerikte neler mi var?\n\n' \
                       '-Konserler\n' \
                       '-Tiyatrolar\n' \
                       '-Opera ve Bale Etkinlikleri\n' \
                       '-Duyurular\n' \
                       '-Deprem Haberleri\n' \
                       '-Firsatlar\n' \
                       '-Izban, Metro, Eshot, Vapur saatleri ve duyurulari\n' \
                       '-Izmirim Kart Bakiye Sorgulama\n' \
                       '-Sinema Seanslari\n-Nobetci Eczaneler\n' \
                       '-Su ve Elektrik Arizalari\n\n' \
                       'Hepsi tek bir uygulamada birlesti. Gule gule kullanin ^^\n\n' \
                       'https://play.google.com/store/apps/details?id=izmirde.hayat'

        Setup.ready_for_post(self)
        actions = ActionChains(self.browser)
        actions.send_keys(text_to_post).perform()
        sleep(5)
        Setup.send_post(self)
        actions.send_keys(Keys.RETURN).perform()

    def kahta_post(self):
        sleep(4)

        kahta = ["1624628781122113", "135970510441878", "1488085274775480",
                 "2388501501384981", "1847520892132643", "264388660669880", "327329167317350", "1831131667169122",
                 "1753788418236087", "kahtagurbet"]

        list = choice(kahta)
        group_url = 'https://www.facebook.com/groups/' + list + '/buy_sell_discussion'

        self.browser.get(group_url)
        print('Posting  on Facebook group: ', group_url)
        sleep(2)

        text_to_post = 'Sayın abilerim, ablalarım, sevgili kardeşlerim,\n' \
                       'Değerli Kahta''mız artık cep telefonumuzda. İlçemizle ilgili: \n\n' \
                       '-İş İlanları\n' \
                       '-Haberler\n' \
                       '-Spor Haberleri\n' \
                       '-2.El Alım Satımlar\n' \
                       '-Restoranlar\n' \
                       '-Taksiler\n' \
                       '-Hava Durumu\n' \
                       '-Nöbetçi Eczaneler\n' \
                       '-Su-Elektrik Arızaları\n' \
                       '-Video Galeri\n' \
                       '-Fotoğraf Galerisi\n\n' \
                       'Hepsi tek bir uygulamada birlesti. Gule gule kullanin ^^\n\n' \
                       'https://play.google.com/store/apps/details?id=kahta.lesi'

        Setup.ready_for_post(self)
        actions = ActionChains(self.browser)
        actions.send_keys(text_to_post).perform()
        sleep(5)
        Setup.send_post(self)
        actions.send_keys(Keys.RETURN).perform()

    def kilkenny_post(self):
        sleep(4)

        kilkenny = ["1430412867205426", "teqsportskilkenny", "631488383595071", "140111069525242", "2140959319539978"]

        list = choice(kilkenny)
        group_url = 'https://www.facebook.com/groups/' + list + '/buy_sell_discussion'

        self.browser.get(group_url)
        print('Posting  on Facebook group: ', group_url)
        sleep(2)

        text_to_post = 'Dear friends,\n' \
                       'Kilkenny City app is now on our mobile phone. About:  \n\n' \
                       '-News\n' \
                       '-Sports\n' \
                       '-Job Applications\n' \
                       '-Concerts\n' \
                       '-Exhibitions\n' \
                       '-Opera\n' \
                       '-Restaurants\n' \
                       '-Weather Forecast\n' \
                       '-Activities\n' \
                       '-Hotels\n\n' \
                       'You will now have easy access to information about :) To download it, just click the link below: \n\n' \
                       'https://play.google.com/store/apps/details?id=kilkenny.city'

        Setup.ready_for_post(self)
        actions = ActionChains(self.browser)
        actions.send_keys(text_to_post).perform()
        sleep(5)
        Setup.send_post(self)
        actions.send_keys(Keys.RETURN).perform()

    def koycegiz_post(self):
        sleep(4)

        koycegiz = ["1825550977701612", "1897150360563786", "koycegiz.kultur.sanat", "dursan48",
                    "101323133800031", "121712639052347", "256353364777997", "429940847106583", "559618474635468",
                    "633634556772916", "stuffforsaleinkoycegiz", "163837907318247", "koycegizliyiz", "769021773258398",
                    "628767133957951"]

        list = choice(koycegiz)
        group_url = 'https://www.facebook.com/groups/' + list + '/buy_sell_discussion'

        self.browser.get(group_url)
        print('Posting  on Facebook group: ', group_url)
        sleep(2)

        text_to_post = 'Güzel Köyceğiz''imin güzel insanları selamlar :)\n\n' \
                       'Yeni uygulamam Köyceğiz İlçesi Play Storeda. İçerikte neler mi var?\n\n' \
                       '-İş İlanları\n' \
                       '-Haberler\n' \
                       '-Restoranlar\n' \
                       '-Hal fiyatları\n' \
                       '-Hava Durumu\n' \
                       '-Yöresel Türküler\n' \
                       '-Nöbetçi Eczaneler\n' \
                       '-Etkinlikler Haberleri\n' \
                       '-Su-Elektrik Arızaları\n' \
                       '-Video Galeri\n' \
                       '-Fotoğraf Galerisi\n\n' \
                       'Hepsi tek bir uygulamada birlesti. Gule gule kullanin ^^\n\n' \
                       'https://play.google.com/store/apps/details?id=com.kyceiz.belediyesi'

        Setup.ready_for_post(self)
        actions = ActionChains(self.browser)
        actions.send_keys(text_to_post).perform()
        sleep(5)
        Setup.send_post(self)
        actions.send_keys(Keys.RETURN).perform()

    def manavgat_post(self):
        sleep(4)

        manavgat = ["152068948488893", "1235365273171718", "945037175514343", "369677536786148",
                    "269742907469940", "930377517038925", "343882795972237", "316784738707982", "1289244694459337",
                    "340120006345513", "1427277477512901", "810606215692882", "1847193255610019", "131161735437",
                    "2000058830216565", "952443884824039", "209939369412433", "antalyateknealimsatim"]

        list = choice(manavgat)
        group_url = 'https://www.facebook.com/groups/' + list + '/buy_sell_discussion'

        self.browser.get(group_url)
        print('Posting  on Facebook group: ', group_url)
        sleep(2)

        text_to_post = 'Güzel Manavgat''ımın güzel insanları selamlar :)\n\n' \
                       'Yeni uygulamam Manavgat İlçesi Play Store''da. İçerikte neler mi var?\n\n' \
                       '-İş İlanları\n' \
                       '-Haberler\n' \
                       '-Hava Durumu\n' \
                       '-Yöresel Türküler\n' \
                       '-Nöbetçi Eczaneler\n' \
                       '-Spor Haberleri\n' \
                       '-Su-Elektrik Arızaları\n' \
                       '-Otobüs Saatleri\n' \
                       '-Fotoğraf Galerisi\n\n' \
                       'Hepsi tek bir uygulamada birlesti. Gule gule kullanin ^^\n\n' \
                       'https://play.google.com/store/apps/details?id=com.manavgat.ilesi'

        Setup.ready_for_post(self)
        actions = ActionChains(self.browser)
        actions.send_keys(text_to_post).perform()
        sleep(5)
        Setup.send_post(self)
        actions.send_keys(Keys.RETURN).perform()

    def midyat_post(self):
        sleep(4)

        midyat = ["sevmektir.hedefimiz", "1657378104514078", "midyatemlak", "1713153065572642",
                  "179094605850162", "1858269431150159", "6368330842", "midyatlilar", "78777212424", "1103062410143331",
                  "644401365905547", "1583251101970768", "225415168351155", "1361704113856904", "586826778193137",
                  "313527519293261", "302366493292190", "1465378513718674", "midyat.ogretmenler", "203263053485392",
                  "581408198549755", "121644048494414", "973061699487117", "1219335254826260", "674538589383416",
                  "midyatsesi", "885727298193074", "1578130905807740", "820976911247639", "1010368612751341",
                  "218407871507361", "2825560511057826", "953375348014387"]

        list = choice(midyat)
        group_url = 'https://www.facebook.com/groups/' + list + '/buy_sell_discussion'

        self.browser.get(group_url)
        print('Posting  on Facebook group: ', group_url)
        sleep(2)

        text_to_post = 'Sayın abilerim, ablalarım, sevgili kardeşlerim,\n' \
                       'Güzel Midyat''ımız artık cep telefonumuzda. İlçemizle ilgili: \n\n' \
                       '-İş İlanları\n' \
                       '-Haberler\n' \
                       '-2.El Alım Satımlar\n' \
                       '-Restoranlar\n' \
                       '-Taksiler\n' \
                       '-Hava Durumu\n' \
                       '-Nöbetçi Eczaneler\n' \
                       '-Su-Elektrik Arızaları\n' \
                       '-Vefat Edenler\n' \
                       '-Fotoğraf Galerisi\n\n' \
                       'Hepsi tek bir uygulamada birlesti. Gule gule kullanin ^^\n\n' \
                       'https://play.google.com/store/apps/details?id=midyat.lesi'

        Setup.ready_for_post(self)
        actions = ActionChains(self.browser)
        actions.send_keys(text_to_post).perform()
        sleep(5)
        Setup.send_post(self)
        actions.send_keys(Keys.RETURN).perform()

    def netherlandspat_post(self):
        sleep(4)

        netherlandspat = ["allexpatsinthenetherlands", "internationalexpatamsterdam", "1041306749227527",
                          "1425158030871295", "laughingatpotatoes", "2393398401", "475997376564057",
                          "889833264399671", "2513882895499019", "expatjobsinthenetherlands",
                          "3391670544390704", "486835584844585", "1510096729269075",
                          "791192707594625",
                          "IndianExpatsInNetherlands", "8139991343", "housesinthenetherlands",
                          "2406969948", "1657109771244718", "1157446251688203",
                          "expatseindhoven", "375891209146726", "iloveamsterdamcity", "expatrepublic",
                          "exploringnetherlands", "284141089612808", "754897328263949", "2204519835",
                          "190296879768427", "1827424617527053", "1503930726289016",
                          "579985732134944", "979765652054041", "2244909725745375", "770298033460235",
                          "expats.eindhoven.nl", "190230194807405", "amsterdam.housing.and.roommates",
                          "605664986795169", "692490407596118", "ExpatsInAmsterdam", "1580853698814943",
                          "ThefunExpatGroupofTheHague", "296739250466742", "rentamsterdam", "1123182838114831",
                          "295804230488520", "478599220659459", "2345051369046723",
                          "expatcommunity", "amsterdamcentrumexpats", "883328028399315", "303940726659024"]

        list = choice(netherlandspat)
        group_url = 'https://www.facebook.com/groups/' + list + '/buy_sell_discussion'

        self.browser.get(group_url)
        print('Posting  on Facebook group: ', group_url)
        sleep(2)

        text_to_post = 'Dear friends,\n' \
                       'Netherlandspat app is now on our mobile phone! About:  \n\n' \
                       '-Concerts\n' \
                       '-Fests\n' \
                       '-Chat\n' \
                       '-Meet New People\n' \
                       '-Rent Bike/Car/House\n' \
                       '-2nd Hand Buy/Sell\n' \
                       '-Sustainability Events\n' \
                       '-Jobs\n' \
                       '-Create Your Own Event\n\n' \
                       'You will now have easy access to information about :) To download it, just click the link below: \n\n' \
                       'https://play.google.com/store/apps/details?id=netherlandspat.app'

        Setup.ready_for_post(self)
        actions = ActionChains(self.browser)
        actions.send_keys(text_to_post).perform()
        sleep(5)
        Setup.send_post(self)
        actions.send_keys(Keys.RETURN).perform()

    def newslingo_post(self):
        sleep(4)

        newslingo = ["481561710258425", "learnenglish.improveyourenglishskills", "565542144351439", "329454095956360",
                     "InnovativeToE", "englishspeakingpracticeesp", "239423810601657", "504633371543410",
                     "358674591314394", "resimlerleingilizcekelimeler", "translationplatform", "125572928772269",
                     "ingilizceplatform", "ydspublishing", "804277272929620", "514863742009381", "englishspeaking24",
                     "329454095956360"]

        list = choice(newslingo)
        group_url = 'https://www.facebook.com/groups/' + list + '/buy_sell_discussion'

        self.browser.get(group_url)
        print('Posting  on Facebook group: ', group_url)
        sleep(2)

        text_to_post = 'Dear friends,\n' \
                       'NewsLingo app is now on our mobile phone.\n\n' \
                       'Are you looking for a fun and easy way to improve your English skills? ' \
                       'Look no further than our new Android app! ' \
                       'Our app lets you read English news articles at your own level, ' \
                       'and even includes a chat feature to practice your conversation skills. ' \
                       'Whether you are a beginner or an advanced learner, our app has something for everyone. ' \
                       'Download it today and start learning English like never before!\n\n' \
                       'https://play.google.com/store/apps/details?id=neuslingo.aplihde'

        Setup.ready_for_post(self)
        actions = ActionChains(self.browser)
        actions.send_keys(text_to_post).perform()
        sleep(5)
        Setup.send_post(self)
        actions.send_keys(Keys.RETURN).perform()

    def oyun_en_post(self):
        sleep(4)

        oyun_en = ["227842967426189", "appandroiddeveloper", "2061280740824150", "3288987951179541",
                   "340386762706349", "470456896341368", "509078119424610", "androidevil", "308278413765308",
                   "ggcreators", "btvgamingofficialgroup", "810855769860840", "511573835572177",
                   "Androidiapa", "blackberry.android", "3954131844626903", "supercarstopspeed",
                   "2205727453048193", "519011588455568",
                   "gamersfrpnet", "501410144060723", "gamdeveloper", "355723031242469",
                   "273058220704295", "streamandpagesharing", "627460971527298", "499649376898165",
                   "185762810426343", "scottsvintagemancavestuff", "318039912719508"]

        list = choice(oyun_en)
        group_url = 'https://www.facebook.com/groups/' + list + '/buy_sell_discussion'

        self.browser.get(group_url)
        print('Posting  on Facebook group: ', group_url)
        sleep(2)

        text_to_post_en = 'Hi all, \n\n\n' \
                       'Retro Arcade Games are now on our smart phone! :) About: \n\n' \
                       '-64 Retro Arcade Games\n' \
                       '-Game Chat Forum\n\n' \
                       'To download please click in the following link: \n\n' \
                       'https://play.google.com/store/apps/details?id=oyunhane.abvl'

        Setup.ready_for_post(self)
        actions = ActionChains(self.browser)
        actions = actions.send_keys(text_to_post_en)
        actions.perform()
        sleep(5)
        Setup.send_post(self)
        actions.send_keys(Keys.RETURN).perform()

    def oyun_tr_post(self):
        sleep(4)

        oyun_tr = ["1502268376707060", "btogtoplulugu", "togog", "oyuncununbilgisayari", "oyungelistiriciler",
                   "AndroidProgramGelistiricileri", "softwaredevsgroup", "programlamaogreniyorum", "MobilGelistiriciler"]

        list = choice(oyun_tr)
        group_url = 'https://www.facebook.com/groups/' + list + '/buy_sell_discussion'

        self.browser.get(group_url)
        print('Posting  on Facebook group: ', group_url)
        sleep(2)

        text_to_post_tr = 'Merhaba arkadaşlar, \n\n\n' \
                       'Retro Arcade oyunlar artık akıllı telefonlarımızda :) İçerikte: \n\n' \
                       '-64 Adet Retro Arcade Oyun\n' \
                       '-Oyun Sohbet Forumu\n\n' \
                       'yer alacaktir. İndirmek için aşağıdaki bağlantıya tıklamanız yeterli: \n\n' \
                       'https://play.google.com/store/apps/details?id=oyunhane.abvl'

        Setup.ready_for_post(self)
        actions = ActionChains(self.browser)
        actions = actions.send_keys(text_to_post_tr)
        actions.perform()
        sleep(5)
        Setup.send_post(self)
        actions.send_keys(Keys.RETURN).perform()

    def saruhanli_post(self):
        sleep(4)

        saruhanli = ["3621892841232883", "625696608295240", "1026591190722191", "362381121834180", "323770108257399",
                     "yeniosmaniye", "1869857186600915", "121237668553899",
                     "1712520632328326", "217516450021487", "877884799676171", "399218583842570",
                     "654117541890123", "112334160927"]

        list = choice(saruhanli)
        group_url = 'https://www.facebook.com/groups/' + list + '/buy_sell_discussion'

        self.browser.get(group_url)
        print('Posting  on Facebook group: ', group_url)
        sleep(2)

        text_to_post = 'Güzel Saruhanlı''mın güzel insanları selamlar :)\n\n' \
                       'Yeni uygulamam Saruhanlı İlçesi Play Storeda. İçerikte neler mi var?\n\n' \
                       '-İş İlanları\n' \
                       '-Haberler\n-Restoranlar\n' \
                       '-Taksiler\n-' \
                       '-Hava Durumu\n-' \
                       '-Nöbetçi Eczaneler\n' \
                       '-Saruhanlı Belediyespor Haberleri\n' \
                       '-Su-Elektrik Arızaları\n' \
                       '-Fotoğraf Galerisi\n\n' \
                       'Hepsi tek bir uygulamada birlesti. Gule gule kullanin ^^\n\n' \
                       'https://play.google.com/store/apps/details?id=com.saruhanl.ilesi'

        Setup.ready_for_post(self)
        actions = ActionChains(self.browser)
        actions.send_keys(text_to_post).perform()
        sleep(5)
        Setup.send_post(self)
        actions.send_keys(Keys.RETURN).perform()

    def soke_post(self):
        sleep(4)

        soke = ["718233511622533", "2198720647021293", "2614247848875259", "183032711887971", "284487099047799",
                "651769814943857", "1083834084969974", "107121203140839", "1652649881642707", "447280948738495",
                "1397160103912534", "624735251481542", "160022984027457", "113022235388425"]

        list = choice(soke)
        group_url = 'https://www.facebook.com/groups/' + list + '/buy_sell_discussion'

        self.browser.get(group_url)
        print('Posting  on Facebook group: ', group_url)
        sleep(2)

        text_to_post = 'Sayın abilerim, ablalarım, sevgili kardeşlerim,\n' \
                       'Güzel Söke''miz artık cep telefonumuzda. İlçemizle ilgili: \n\n' \
                       '-İş İlanları\n' \
                       '-Haberler\n' \
                       '-Restoranlar\n' \
                       '-Taksiler\n' \
                       '-Hava Durumu\n' \
                       '-Nöbetçi Eczaneler\n' \
                       '-Sökespor Haberleri\n' \
                       '-Su-Elektrik Arızaları\n' \
                       '-Vefat Edenler\n' \
                       '-Fotoğraf Galerisi\n\n' \
                       'Hepsi tek bir uygulamada birlesti. Gule gule kullanin ^^\n\n' \
                       'https://play.google.com/store/apps/details?id=ske.lesi'

        Setup.ready_for_post(self)
        actions = ActionChains(self.browser)
        actions.send_keys(text_to_post).perform()
        sleep(5)
        Setup.send_post(self)
        actions.send_keys(Keys.RETURN).perform()

    def tavsanli_post(self):
        sleep(4)

        tavsanli = ["371521519658763", "2918986854785156", "203459223082833", "2095593284007825", "228511447587069",
                    "1173935345995444", "318440788856233", "1783132881980335", "142750250061341", "1485263505113239",
                    "516140542385739", "227459675083900", "723145614498513", "1736313896533707",
                    "243999833363938", "1009042875800957", "216310852991424", "438267427067482"]

        list = choice(tavsanli)
        group_url = 'https://www.facebook.com/groups/' + list + '/buy_sell_discussion'

        self.browser.get(group_url)
        print('Posting  on Facebook group: ', group_url)
        sleep(2)

        text_to_post = 'Güzel Tavşanlı''mın güzel insanları selamlar :)\n\n' \
                       'Yeni uygulamam Tavşanlı İlçesi Play Storeda. İçerikte neler mi var?\n\n' \
                       '-İş İlanları\n' \
                       '-Haberler\n' \
                       '-Hava Durumu\n' \
                       '-Nöbetçi Eczaneler\n' \
                       '-Tavşanlı Belediyespor Haberleri\n' \
                       '-Elektrik Arızaları\n' \
                       '-Otobüs Saatleri\n' \
                       '-Fotoğraf Galerisi\n\n' \
                       'Hepsi tek bir uygulamada birlesti. Gule gule kullanin ^^\n\n' \
                       'https://play.google.com/store/apps/details?id=com.tavanl.ilesi'

        Setup.ready_for_post(self)
        actions = ActionChains(self.browser)
        actions.send_keys(text_to_post).perform()
        sleep(5)
        Setup.send_post(self)
        actions.send_keys(Keys.RETURN).perform()

    def torbali_post(self):
        sleep(4)

        torbali = ["1674152716182011", "TRMEHMET", "tobedak", "3737007473081269",
                   "1719536631616508", "531570480830339", "815312195557528", "213121952562502",
                   "1138779186487991", "160202221998957", "652045991632541",
                   "194760451278928", "1581787365415048", "281538418715072", "827540141115373",
                   "343288555591", "275915996290129", "624143651345231"]

        list = choice(torbali)
        group_url = 'https://www.facebook.com/groups/' + list + '/buy_sell_discussion'

        self.browser.get(group_url)
        print('Posting  on Facebook group: ', group_url)
        sleep(2)

        text_to_post = 'Güzel Torbalı''mın güzel insanları selamlar :)\n\n' \
                       'Yeni uygulamam Torbalı İlçesi Play Storeda. İçerikte neler mi var?\n\n' \
                       '-İş İlanları\n' \
                       '-Haberler\n' \
                       '-Restoranlar\n' \
                       '-Taksiler\n' \
                       '-Hava Durumu\n' \
                       '-Yöresel Türküler\n' \
                       '-Nöbetçi Eczaneler\n' \
                       '-Torbalıspor Haberleri\n' \
                       '-Su-Elektrik Arızaları\n' \
                       '-Vefat Edenler\n' \
                       '-Fotoğraf Galerisi\n\n' \
                       'Hepsi tek bir uygulamada birlesti. Gule gule kullanin ^^\n\n' \
                       'https://play.google.com/store/apps/details?id=torbal.lesi'

        Setup.ready_for_post(self)
        actions = ActionChains(self.browser)
        actions.send_keys(text_to_post).perform()
        sleep(5)
        Setup.send_post(self)
        actions.send_keys(Keys.RETURN).perform()

    def close_browser(self):
        self.browser.close()

r = Run()
r.setup()

array = [r.alasehir_post, r.ayrancilar_post, r.boostify_post, r.esme_post, r.goztepe_post, r.halisaha_post, r.izmir_post,
         r.kahta_post, r.kilkenny_post, r.koycegiz_post, r.manavgat_post, r.midyat_post, r.netherlandspat_post,
         r.newslingo_post, r.oyun_en_post, r.oyun_tr_post, r.saruhanli_post, r.soke_post, r.tavsanli_post, r.torbali_post
         ]

list = sample(array, len(array))
for i in range(1, 7):
    list[i]()