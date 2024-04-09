import requests
import sys


def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"\033[92m{url}: is reachable and working fine. \033[0m")

        else:
            print(f"\033[91m{url}: returned a non-OK status code: {response.status_code}\033[0m")

    except requests.RequestException as e:
        print(f"\033[93m{url}: could not be reached. Exception: {e}\033[0m")

    # List of website domains to check
websites = [
    "voteyesforregionaltransit.com",
    "peopleoftheinfinitefires.com",
    "usoffshorewindconference.com",
    "protectrihealthcare.org",
    "documentedsuccess.org",
    "gilbertfireapp.com",
    "ubrandapp.com",
    "broadswordstudentadvantage.com",
    "translationsintupperware.com",
    "godshousefilm.com",
    "operationworkwarriors.org",
    "crowdsourcethecourse.com",
    "magicformulatinvesting.com",
    "pitchlebroncontest.com",
    "shurook.org",
    "letstalkaboutthefamily.org",
    "aitempeaz.org",
    "la-roots.com",
    "makandarainmaker.com",
    "relishurbanag.com",
    "azsaveourfuturenow.com",
    "lunchadorsunite.com",
    "charlestonwestside.org",
    "detainedbyus.org",
    "ileadsuccess.org",
    "awidemercy.com",
    "arkansasfreethinkers.com",
    "deplorablesmag.com",
    "scarpatiindiantaming.com",
    "lexingtonepiscopalian.com",
    "motorcitymedicalmission.org",
    "itseasybeinggreenmovie.com",
    "ederalnewsnetwork.com",
    "firesamperlozzo.com",
    "ceoclubteam.com",
    "myhauntsite.com",
    "downhomeatx.com",
    "hopsctch.com",
    "frederickwschmidt.com",
    "warroomalerts.com",
    "tsalagithinktank.com",
    "everyonesreading.org",
    "radiationzero.com",
    "happyhoundco.org",
    "wedetailplanes.com",
    "30daysonjetblue.com",
    "yweddyco.org",
    "casadepregrinos.org",
    "noahpurify.com",
    "hoenixchineseweek.org",
    "keepourwellsclean.org",
    "keepkingswoodpark.com",
    "ewseum.org",
    "acrossthebridgearts.com",
    "civilrightsmuesum.org",
    "humantiestennessee.org",
    "hubbelltaxreturns.com",
    "cdemocratandchronicle.com",
    "stone4judge.com",
    "eatjoesny.com",
]

# Check each website
for website in websites:
    check_website("https://" + website)  # You may need to use "https://" if the websites use SSL.
