import sys
sys.path.append(r'C:\\Projects\\Sosyal\\Facebook')
from init import *

class Run:
    def setup(self):
        Setup.login(self)

    def alasehir_post(self):
        sleep(4)

        alasehir = ["2482168202011446", "325220324225839", "1544979455609019",
                    "826697807434059", "728139434428844", "566967630721933",
                    "alasehirkiraliksatilikgayrimenkul"]

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
                 "568306859986232", "177753004080514", "1804913393067179", "331835926980955",
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
                      "1586603538128730", "2240938972810805", "1192618434087801", "238656837475420",
                      "333284927980868", "2460181387617813", "1068832396815501", "207248929672296", "131859181017957",
                      "453756859346524", "712485366009386", "3441863649184399"]

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

    def ege_post(self):
        sleep(4)

        sozluk = ["egeevarkadasi", "1430596860532102", "254187258119986", "TopluluklarEge", "379934872198429", "egenso",
                  "egeogrencileri", "Egeparttime", "18019857931", "215182778504930", "5272033731", "1480104958897419",
                  "430556560443037", "egealimvesatim", "kucukmendereshavzasi", "egeunialimsatim", "66151379408",
                  "ulitege", "1382454552016358", "5227134462", "220261332183076", "egeunibisiklet", "deuevarkadasi",
                  "17657058816", "169716939731794", "1207874752574624", "9252779851", "6104626645", "18659112496",
                  "748088955207007", "161523990674375", "226917504020810", "egeuniversitesigezi", "172110019647"]

        list = choice(sozluk)
        group_url = 'https://www.facebook.com/groups/' + list + '/buy_sell_discussion'

        self.browser.get(group_url)
        print('Posting  on Facebook group: ', group_url)
        sleep(2)

        text_to_post = 'Ege Üniversitesi sözlük uygulaması artık Play Market''te! :)\n' \
                       'İçerikte:\n\n' \
                       '-Paylaşım yapabileceğiniz sözlük bölümü\n' \
                       '-2. El Alım Satım\n' \
                       '-İş İlanları\n' \
                       '-Ev Arkadaşı Bulma\n' \
                       '-Çevrenizdeki Sözlük Kullanıcılarını Görüntüleme\n' \
                       '-Sohbet Özelliği\n' \
                       'özellikle mevcuttur. İyi günlerde kullanmanız temennimizle :)\n\n' \
                       'https://play.google.com/store/apps/details?id=ege.sozluk'

        Setup.ready_for_post(self)
        actions = ActionChains(self.browser)
        actions.send_keys(text_to_post).perform()
        sleep(5)
        Setup.send_post(self)
        actions.send_keys(Keys.RETURN).perform()

    def esme_post(self):
        sleep(4)

        esme = ["762951934454642", "452448632246858", "1030065057498284", "dervislikoyu",
                "422335515606986", "1562201027378354", "2323050764478917", "531806510545262",
                "574000413548546", "546914658780031", "1986018184978764", "sivaslialsat",
                "796198000551872", "2462719980412101", "3115960435151650", "2302795416666275", "1751474938464718",
                "599522303449499", "180888425302580", "515028112596989", "694003467429707"]

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

        goztepe = ["330761873609935", "256830128397118", "2730901190498018", "208028558536", "1482691535388761",
                   "1540597852877697", "159424877529948", "332225360477262", "210922582375185", "575389225857771",
                   "1194038040638929", "wwwisoookubra", "229136775939229", "259943855903893", "680538306155255",
                   "416889008451550", "259820858593897", "453152851683911", "257968525316500", "1119653814739937",
                   "156296471231004", "384831866221969", "202802114364116", "368964550120282", "632261113598528",
                   "278916619179669", "169197057727346", "1743504639157693", "122154371830585", "936992506365153",
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
                    "1526281577639275", "500219933389663", "serefhalisaha", "1323820704398716", "186292634788799",
                    "1374235479480096", "132196480204037", "819641191404421", "227057034339953", "255780481194859",
                    "710886928950249", "247446628721533", "109456339122304", "KonyaHaliSahaRakipBul", "1576233845995645",
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

        izmir = ["izmirelektronikalimsatimtakas", "izmirxizmir", "1499452027011704", "251687191870465",
                 "karsiyakabitpazari", "izmirikincielpazarim", "izmirenglishspeakers", "izmirbilgisayar",
                 "1624712331149186", "tam35sohbet", "izmirsondakika", "1786050418326386", "286039838397195",
                 "629100274121495", "1221311804559488", "1549495335274303", "3391919157530736", "izmirikincielgrup",
                 "251687191870465", "izmirdecevirme", "2125911384165459", "845375905550243",
                 "1827537364172661", "1728725010490278", "5888323829", "305154173262002", "167376063347023",
                 "1797464497200766", "601714939977538", "devlettiyatrosuizmir", "2059423444286714", "226585790710064",
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

        kahta = ["1624628781122113", "kahtakursu", "135970510441878", "kahtayerelhaberler", "1488085274775480",
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

        kilkenny = ["1430412867205426", "2825610674352955", "148605668543143", "teqsportskilkenny",
                    "1587632794804215", "140111069525242", "631488383595071", "2140959319539978"]

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

        manavgat = ["1977654352501132", "152068948488893", "1235365273171718", "1235437996536777",
                    "269742907469940", "930377517038925", "216353675048716", "291503291352138", "343882795972237",
                    "340120006345513", "1427277477512901", "810606215692882", "1847193255610019", "131161735437",
                    "2000058830216565", "952443884824039", "209939369412433", "316784738707982", "1289244694459337",
                    "945037175514343", "369677536786148", "407676326728979", "antalyateknealimsatim"]

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

        midyat = ["366476150457472", "sevmektir.hedefimiz", "1657378104514078", "midyatemlak", "1713153065572642",
                  "179094605850162", "1858269431150159", "6368330842", "midyatlilar",
                  "644401365905547", "1583251101970768", "225415168351155", "1361704113856904",
                  "313527519293261", "302366493292190", "1465378513718674", "midyat.ogretmenler",
                  "581408198549755", "121644048494414", "973061699487117", "1219335254826260",
                  "midyatsesi", "885727298193074", "1578130905807740", "820976911247639", "1010368612751341",
                  "203263053485392", "586826778193137", "78777212424", "1103062410143331", "1767734176819749",
                  "218407871507361", "2825560511057826", "674538589383416", "953375348014387", "1276311579152352"]

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
                          "Best.Jobs.Netherlands", "3391670544390704", "486835584844585", "1510096729269075",
                          "vacantes.netherlands", "UnitedExpatsoftheNetherlands", "791192707594625",
                          "IndianExpatsInNetherlands", "8139991343", "housesinthenetherlands",
                          "2406969948", "JobsinHolland", "1657109771244718", "1157446251688203",
                          "expatseindhoven", "375891209146726", "iloveamsterdamcity", "expatrepublic",
                          "exploringnetherlands", "284141089612808", "754897328263949", "2204519835",
                          "190296879768427", "1827424617527053", "288221731281767", "1503930726289016",
                          "579985732134944", "979765652054041", "2244909725745375", "770298033460235",
                          "expats.eindhoven.nl", "190230194807405", "amsterdam.housing.and.roommates",
                          "605664986795169", "692490407596118", "ExpatsInAmsterdam", "1580853698814943",
                          "ThefunExpatGroupofTheHague", "296739250466742", "rentamsterdam", "1123182838114831",
                          "295804230488520", "478599220659459", "2345051369046723", "765584943917713",
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

    def oyun_en_post(self):
        sleep(4)

        oyun_en = ["227842967426189", "appandroiddeveloper", "2061280740824150", "3288987951179541", "1507491152850856",
                   "340386762706349", "470456896341368", "509078119424610", "androidevil", "308278413765308",
                   "ggcreators", "btvgamingofficialgroup", "810855769860840", "831204153907361", "511573835572177",
                   "1518367058334244", "Androidiapa", "blackberry.android", "3954131844626903", "supercarstopspeed",
                   "2205727453048193", "mobileappdevelopments", "519011588455568", "mobiloids", "thegamerlife",
                   "gamersfrpnet", "501410144060723", "gamdeveloper", "355723031242469", "319019998906454",
                   "273058220704295", "streamandpagesharing", "3dswiiugamers", "627460971527298", "499649376898165",
                   "185762810426343", "scottsvintagemancavestuff", "318039912719508", "152228903476838"]

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

        oyun_tr = ["1249974598366070", "androidoyun", "AndroidGelistirme", "GeneralMobileAndroidOne4G",
                   "AndroidProgramGelistiricileri", "softwaredevsgroup",
                   "394535784235625", "unlostv", "1028228647188038", "MobilGelistiriciler", "oyuncununbilgisayari",
                   "trcastleclash", "btogtoplulugu", "1725332541112353", "togog", "MtaServerlers", "oyungelistiriciler",
                   "1511527392393141", "programlamaogreniyorum", "1502268376707060", "219888054757307",
                   "arenaofvalornoss"]

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

    def pet_post(self):
        sleep(4)

        pet = ["huncalife35", "474842530016186", "kedikopekkussahiplendirme", "1065479390549253", "172459679848313",
               "izmirevcilhayvansahiplendirme", "607228792818322", "1317939498358641", "1256977574457496",
               "788584284552115", "533015283518913", "233571787510866", "2088427014800493", "412783958820720",
               "827540141115373", "1428188010818868", "594771670732498", "KopekSahiplendirme", "2235052526771916",
               "397204243774401", "hekimhanemersin", "163263510678375", "petdost06", "283106478550596",
               "2015921291971098", "2135577956687291", "867425070105002", "KopekSahiplendirme"]

        list = choice(pet)
        group_url = 'https://www.facebook.com/groups/' + list + '/buy_sell_discussion'

        self.browser.get(group_url)
        print('Posting  on Facebook group: ', group_url)
        sleep(2)

        text_to_post = 'Merhaba arkadaşlar. PetSahiplen uygulaması artık Play Store''da! :)\n\n' \
                       'PetSahiplen ile artık evcil hayvanınıza sahip bulmak ve evcil hayvan sahiplenmek çok kolay. İçerikte: \n\n' \
                       '-Sahiplendirme Forumu\n' \
                       '-Kayıp Hayvan İhbar Forumu\n' \
                       '-Sohbet Özelliği\n' \
                       '-Çevrenizdeki Kişileri Görüntüleme\n' \
                       '-Haberler\n\n' \
                       'yer almaktadır. İyi günlerde kullanmanız temennimle ^^\n\n' \
                       'https://play.google.com/store/apps/details?id=petsahiplen.appxcb'

        Setup.ready_for_post(self)
        actions = ActionChains(self.browser)
        actions.send_keys(text_to_post).perform()
        sleep(5)
        Setup.send_post(self)
        actions.send_keys(Keys.RETURN).perform()

    def saruhanli_post(self):
        sleep(4)

        saruhanli = ["3621892841232883", "625696608295240", "1026591190722191", "362381121834180", "323770108257399",
                     "yeniosmaniye", "1869857186600915", "121237668553899",
                     "1712520632328326", "2593150607677028", "217516450021487", "877884799676171", "399218583842570",
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
                "651769814943857", "360540204506455", "1083834084969974", "107121203140839", "1652649881642707",
                "1397160103912534", "624735251481542", "160022984027457", "331835926980955", "113022235388425",
                "447280948738495"]

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
                    "516140542385739", "383714302106284", "227459675083900", "723145614498513", "1736313896533707",
                    "1407897382839919", "243999833363938", "1009042875800957", "216310852991424",
                    "809726322875281", "438267427067482"]

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

        torbali = ["1674152716182011", "TRMEHMET", "3815981261797816", "tobedak", "3737007473081269",
                   "1719536631616508", "531570480830339", "815312195557528", "213121952562502",
                   "1138779186487991", "160202221998957", "461181397343488", "652045991632541",
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

    def ucacaksin_post(self):
        sleep(4)

        ucacaksin = ["ucakbiletleri", "220561833134593", "webbilet", "366226913916907", "indirimlibilet.net",
                     "218051502116675", "1401292690119260", "2180149602228186", "econombilet", "1407977396175349",
                     "183354628665079", "1450214861885604", "319379728089143", "ucuzucakbileti", "503111189722019",
                     "123117417858654", "1259712310798927", "1589449664675322", "1772796709633633", "644639619043245",
                     "425123868339887", "11001805838", "229674040559521", "1112588998785166", "723790614360147",
                     "1917508198519480", "379081745533897", "723790614360147", "339984579545601"]

        list = choice(ucacaksin)
        group_url = 'https://www.facebook.com/groups/' + list + '/buy_sell_discussion'

        self.browser.get(group_url)
        print('Posting  on Facebook group: ', group_url)
        sleep(2)

        text_to_post = 'Değerli abilerim, sevgili kardeşlerim. Ucacaksin uygulaması artık Play Store''da! :)\n\n' \
                       'İçerikte: \n\n' \
                       '-En Ucuz Ucak Bileti Firsatlari\n' \
                       '-Indirim Kuponlari\n' \
                       '-Sohbet Ozelligi\n\n' \
                       'yer almaktadır. İyi günlerde kullanmanız temennimle ^^\n\n' \
                       'https://play.google.com/store/apps/details?id=ucacaksin.ucacaksin'

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
array = [r.alasehir_post, r.ayrancilar_post, r.esme_post, r.goztepe_post, r.halisaha_post, r.izmir_post,
         r.kahta_post, r.kilkenny_post, r.koycegiz_post, r.manavgat_post, r.midyat_post, r.netherlandspat_post,
         r.oyun_en_post, r.oyun_tr_post, r.pet_post, r.saruhanli_post, r.soke_post, r.tavsanli_post, r.torbali_post,
         r.ucacaksin_post]

for i in range(len(array)):
    list = sample(array, len(array))
    list[i]()
