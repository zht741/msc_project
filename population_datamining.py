import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')


import django
django.setup()
from datamining.models import Category, Page

def populate():
    datamining_pages = [
        {'title': 'A Survey of Text Mining Techniques and Applications ',
        'url':'http://www.jetwi.us/uploadfile/2014/1230/20141230112729939.pdf',
        'views': 30,
        'sum' : 30,
        'num' : 7,
        }, 
        {'title':'Customer behavior and decision making in the refurbishment industry‐a data mining approach',
        'url':'https://www.tandfonline.com/doi/abs/10.3846/jcem.2010.07',
        'views': 56,
        'sum' : 20,
        'num' : 3,
        },  
        {'title':'A Financial Data Mining Model for Extracting Customer Behavior',
        'url':'https://hrcak.srce.hr/file/106497',
        'views': 90,
        'sum' : 120,
        'num' : 13,
        },   
        {'title': 'Improving Customer Relationship Management Using Data Mining',
        'url':'http://www.ijmlc.org/papers/256-L40070.pdf',
        'views':2290,
        'sum' : 12,
        'num' : 2,
        }, ]


    EFinance_pages = [
        {'title':'E-Finance in Emerging Markets: Is Leapfrogging Possible?',
         'url':'https://papers.ssrn.com/sol3/papers.cfm?abstract_id=280794',
         'views': 8988,
        'sum' : 421,
        'num' : 73,
        }, 
        {'title':'E‐Finance for Development: Global Trends, National Experience and SMEs',
         'url':'https://www.researchgate.net/profile/Janet-Toland/publication/228752792_E-Finance_for_Development_Global_Trends_National_Experience_and_SMEs/links/55d786cb08aec156b9aa1595/E-Finance-for-Development-Global-Trends-National-Experience-and-SMEs.pdf',
         'views': 78,
        'sum' : 49,
        'num' : 7,
        }, 
    ]
    Finance_pages = [
        {'title':'The History of Finance',
         'url':'https://jpm.pm-research.com/content/25/4/95.short',
         'views': 7890,
        'sum' : 121,
        'num' : 13,
        }, 
        {'title':'The Economics of Structured Finance',
         'url':'https://pubs.aeaweb.org/doi/pdfplus/10.1257/jep.23.1.3',
         'views': 56,
        'sum' : 48,
        'num' : 7,
        }, 
    ]

    Currency_pages = [
        {'title':'Currency Unions and International Integration',
         'url':'https://www.nber.org/papers/w7872',
         'views': 339,
        'sum' : 544,
        'num' : 77,
        }, 
        {'title':"Currency Value",
         'url':'https://academic.oup.com/rfs/article-abstract/30/2/416/2669968',
         'views': 199,
        'sum' : 421,
        'num' : 76,
        }, 
        {'title':"The crypto-currency",
         'url':'https://cryptome.org/0005/bitcoin-who.pdf',
         'views': 239,
        'sum' : 17,
        'num' : 3,
        }, 
    ]
    BigData_pages = [
        {'title': 'The big challenges of big data',
        'url':'https://www.nature.com/articles/498255a',
        'views': 1069,
        'sum' : 121,
        'num' : 13,
        },  
        {'title':'Big Data: The Management Revolution',
        'url':'https://wiki.uib.no/info310/images/4/4c/McAfeeBrynjolfsson2012-BigData-TheManagementRevolution-HBR.pdf',
        'views': 789,
        'sum' : 1209,
        'num' : 139,
        },  
        {'title':'Challenges of Big Data analysis',
        'url':'https://academic.oup.com/nsr/article/1/2/293/1397586?login=true',
        'views': 90,
        'sum' : 43,
        'num' : 13,
        }, 
        {'title': 'BIG DATA ANALYTICS',
        'url':'https://vivomente.com/wp-content/uploads/2016/04/big-data-analytics-white-paper.pdf',
        'views':449,
        'sum' : 120,
        'num' : 13,
        }, 
    ]
 
    

    cats = {'datamining': {'pages': datamining_pages, 'views': 128, 'likes': 64},
            'EFinance ': {'pages': EFinance_pages, 'views': 32, 'likes': 16},
            'Finance': {'pages': Finance_pages, 'views': 16, 'likes': 7},
            'Currency': {'pages': Currency_pages, 'views': 30, 'likes': 12},
            'BigData': {'pages': BigData_pages, 'views': 170, 'likes': 89},
            }

    
    for cat, cat_data in cats.items():
        c = add_cat(cat, views=cat_data['views'], likes=cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], views = p['views'],sum=p['sum'],num=p['num'],ave=round(p['sum']/p['num'],2))

    for c in Category.objects.all():
        for p in Page.objects.filter(category = c):
            print(f'-{c}: {p}')


def add_page(cat, title, url, views=0,num=0,sum=0,ave=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.sum = sum
    p.num = num
    p.ave = ave
    p.save()
    return p

def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

if __name__ == '__main__':
    print('Starting datamining population script...')
    populate()
