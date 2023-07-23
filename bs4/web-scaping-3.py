# navigating through html tree 
from bs4 import BeautifulSoup
import re
import requests


# HTML From Website
url = "https://species.wikimedia.org/wiki/Chroicocephalus_ridibundus"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

tbody = doc.tbody
print(tbody)
trs = tbody.contents
print('===============')
print(trs[0])
print(trs[1])
print(trs[2])
print(trs[1].next_sibling)
print('===============')
print(trs[1].replace_with_children)
print('===============')
print(tbody.children)


#  <span class="mw-headline" id="Vernacular_names">Vernacular names</span>
#  <div style="padding:0 10px; -moz-column-count: 2; -moz-column-gap: 40px; -moz-column-rule: 1px solid #aaa; -webkit-column-count: 2; -webkit-column-gap: 40px; -webkit-column-rule: 1px solid #aaa; column-count: 2; column-gap: 40px; column-rule: 1px solid #aaa; border:1px solid #aaa; background:#f9f9f9; font-size:90%">
# <b>Afrikaans:</b>&nbsp;Swartkopmeeu<br><b>العربية:</b>&nbsp;النورس أسود الرأس<br><b>asturianu:</b>&nbsp;Gavilueta Glayadora<br><b>azərbaycanca:</b>&nbsp;Adi qağayı<br><b>Boarisch:</b>&nbsp;Lochméwen<br><b>беларуская:</b>&nbsp;Чайка-рыбачка<br><b>български:</b>&nbsp;Речна чайка<br><b>বাংলা:</b>&nbsp;কালামাথা গাঙচিল<br><b>brezhoneg:</b>&nbsp;Ar gouelan penn du<br><b>català:</b>&nbsp;Gavina riallera<br><b>čeština:</b>&nbsp;Racek chechtavý<br><b>Cymraeg:</b>&nbsp;Gwylan Benddu<br><b>dansk:</b>&nbsp;Hættemåge<br><b>Deutsch:</b>&nbsp;Lachmöwe<br><b>ދިވެހިބަސް:</b>&nbsp;Boakalhu Gohorukey<br><b>Ελληνικά:</b>&nbsp;Χωραφόγλαρος<br><b>English:</b>&nbsp;Black-headed Gull<br><b>Esperanto:</b>&nbsp;Ridmevo<br><b>español:</b>&nbsp;Gaviota Reidora<br><b>eesti:</b>&nbsp;Naerukajakas<br><b>euskara:</b>&nbsp;Antxeta mokogorri<br><b>suomi:</b>&nbsp;Naurulokki<br><b>føroyskt:</b>&nbsp;Fransaterna<br><b>Nordfriisk:</b>&nbsp;Suarthoodet kub<br><b>français:</b>&nbsp;Mouette rieuse<br><b>Frysk:</b>&nbsp;Kob<br><b>Gaeilge:</b>&nbsp;Faoileán an chaipín<br><b>Gàidhlig:</b>&nbsp;Fhaoileag a'chinn duibh<br><b>galego:</b>&nbsp;Gaivota chorona<br><b>Gaelg:</b>&nbsp;Foillan kione doo<br><b>עברית:</b>&nbsp;שחף אגמים<br><b>hrvatski:</b>&nbsp;Obični galeb<br><b>magyar:</b>&nbsp;Dankasirály<br><b>հայերեն:</b>&nbsp;Որոր սովորական<br><b>Bahasa Indonesia:</b>&nbsp;Camar kepala hitam<br><b>íslenska:</b>&nbsp;Hettumáfur<br><b>italiano:</b>&nbsp;Gabbiano comune<br><b>日本語:</b>&nbsp;ユリカモメ<br><b>ქართული:</b>&nbsp;ტბის თოლია<br><b>қазақша:</b>&nbsp;Кєл шағаласы<br><b>kalaallisut:</b>&nbsp;Nasalik<br><b>한국어:</b>&nbsp;붉은부리갈매기<br><b>Lëtzebuergesch:</b>&nbsp;Laachméiw<br><b>lietuvių:</b>&nbsp;Rudagalvis kiras<br><b>latviešu:</b>&nbsp;Lielais ķīris<br><b>македонски:</b>&nbsp;Обичен галеб<br><b>മലയാളം:</b>&nbsp;ചെറിയ കടല്‍ കാക്ക<br><b>монгол:</b>&nbsp;Хүрэн толгойт цахлай - ᠬᠦᠷᠡᠩ ᠲᠣᠯᠣᠭᠠᠢᠢᠲᠣ ᠴᠠᠬᠣᠯᠠᠢ<br><b>Bahasa Melayu:</b>&nbsp;Camar kepala hitam<br><b>Malti:</b>&nbsp;Gawwija Rasha Kannella<br><b>Nederlands:</b>&nbsp;Kokmeeuw<br><b>norsk nynorsk:</b>&nbsp;Hettemåse<br><b>norsk:</b>&nbsp;Hettemåke<br><b>polski:</b>&nbsp;Mewa śmieszka<br><b>português:</b>&nbsp;Guincho-comum<br><b>rumantsch:</b>&nbsp;Muetta rienta<br><b>română:</b>&nbsp;Pescăruş râzător<br><b>русский:</b>&nbsp;Озёрная чайка<br><b>davvisámegiella:</b>&nbsp;Gahperbáiski<br><b>slovenčina:</b>&nbsp;Čajka smejivá<br><b>slovenščina:</b>&nbsp;Rečni galeb<br><b>shqip:</b>&nbsp;Pulebardha e zakonshme<br><b>српски / srpski:</b>&nbsp;Obicni galeb - Обични галеб<br><b>svenska:</b>&nbsp;Skrattmås<br><b>Kiswahili:</b>&nbsp;Shakwe Kichwa-kahawia<br><b>தமிழ்:</b>&nbsp;கருந்தலை கடல் காக்கை<br><b>ไทย:</b>&nbsp;นกนางนวลขอบปีกขาว<br><b>Türkçe:</b>&nbsp;Karabaş martı<br><b>українська:</b>&nbsp;Звичайний мартин<br><b>Tiếng Việt:</b>&nbsp;Mòng biển đầu đen<br><b>中文:</b>&nbsp;红嘴鸥<br></div>

vNames = doc.find_all(["span"], id="Vernacular_names" )
print('===============')
print(vNames[0].parent.next_sibling)
