from fastapi import FastAPI,Response, Body
from fastapi.middleware.cors import CORSMiddleware
import datetime
import json
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fake_db = [
{"id":1,"name":"car1","ctime":"2020-6-15"},
{"id":2,"name":"car2","ctime":"2020-6-15"},
{"id":3,"name":"car3","ctime":"2020-6-15"},
{"id":4,"name":"car4","ctime":"2020-6-15"},
{"id":5,"name":"car5","ctime":"2020-6-15"}
]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/getData")
def read_item():
    return fake_db

@app.post("/postData")
def post_item(name=Body(...),
              id = Body(...)):
    print(id)
    fake_db.append({"id":id,"name":name,"ctime":"2020-6-15"})
    return fake_db

@app.post("/del")
def del_item(index = Body(...)):
    fake_db.pop(index['index'])
    return fake_db

@app.get('/lunbotu')
def get_lunbotu():
    data = [
        {'img': 'http://img5.imgtn.bdimg.com/it/u=208926184,1909506007&fm=26&gp=0.jpg'},
        {'img': 'http://img4.imgtn.bdimg.com/it/u=3324177140,1929677718&fm=26&gp=0.jpg'},
        {'img': 'http://img3.imgtn.bdimg.com/it/u=3222547049,3569275220&fm=26&gp=0.jpg'},
    ]
    return data


@app.get('/newslist')
def get_newslist():
    newslist = [
        {'id': 0,
        'title': '抓猫行动现在开始！',
        'post_time': datetime.datetime.now().strftime('%F %T'),
         'time': 0,
         'img': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1592815444850&di=0cdffe019bc22c64ceabe7cff4aa229a&imgtype=0&src=http%3A%2F%2Fb.zol-img.com.cn%2Fdesk%2Fbizhi%2Fstart%2F3%2F1382685593976.jpg'
         },
        {'id': 1,
         'title': '抓猫行动现在开始！',
         'post_time': datetime.datetime.now().strftime('%F %T'),
         'time': 1,
         'img': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1592815444850&di=0cdffe019bc22c64ceabe7cff4aa229a&imgtype=0&src=http%3A%2F%2Fb.zol-img.com.cn%2Fdesk%2Fbizhi%2Fstart%2F3%2F1382685593976.jpg'

         },
        {'id': 2,
         'title': '抓猫行动现在开始！',
         'post_time': datetime.datetime.now().strftime('%F %T'),
         'time': 2,
         'img': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1592815444850&di=0cdffe019bc22c64ceabe7cff4aa229a&imgtype=0&src=http%3A%2F%2Fb.zol-img.com.cn%2Fdesk%2Fbizhi%2Fstart%2F3%2F1382685593976.jpg'
         }

    ]
    return newslist

newsinfos = [
    {'id': 0, 'title': '抓猫行动0', 'content': 'Pythonista_w','click': 0, 'time': datetime.datetime.now().strftime('%F %T')},
    {'id': 1, 'title': '抓猫行动1', 'content': 'Pythonista_x','click': 1, 'time': datetime.datetime.now().strftime('%F %T')},
    {'id': 2, 'title': '抓猫行动2', 'content': 'Pythonista_b','click': 2, 'time': datetime.datetime.now().strftime('%F %T')},
]

@app.get('/getnewsinfo/{id}')
def get_newsinfo(id):
    for i in newsinfos:
        if i['id'] == int(id):
            return newsinfos[int(id)]

comments = [
    {'id': 0, 'content': '啥也不是1-0', 'item_id': 1 ,'name': 'n1', 'index': 1},
    {'id': 1, 'content': '啥也不是1-1', 'item_id': 1 ,'name': 'n2', 'index': 1},
    {'id': 2, 'content': '啥也不是1-2', 'item_id': 1 ,'name': 'n2', 'index': 1},
    {'id': 3, 'content': '啥也不是1-0', 'item_id': 1, 'name': 'n1', 'index': 1},
    {'id': 4, 'content': '啥也不是1-1', 'item_id': 1, 'name': 'n2', 'index': 1},
    {'id': 5, 'content': '啥也不是1-2', 'item_id': 1, 'name': 'n2', 'index': 2},
    {'id': 6, 'content': '啥也不是1-0', 'item_id': 1 ,'name': 'n1', 'index': 2},
    {'id': 7, 'content': '啥也不是1-1', 'item_id': 1 ,'name': 'n2', 'index': 2},
    {'id': 8, 'content': '啥也不是1-2', 'item_id': 1 ,'name': 'n2', 'index': 2},

    {'id': 1, 'content': '啥也不是0-1', 'item_id': 0 ,'name': 'n3'},
    {'id': 2, 'content': '啥也不是0-2', 'item_id': 0 ,'name': 'n4'},

    {'id': 1, 'content': '啥也不是2-1', 'item_id': 2 ,'name': 'n5'},
    {'id': 2, 'content': '啥也不是2-2', 'item_id': 2 ,'name': 'n4'},
]

@app.get('/comment/{id}/{index}')
def get_comment(id,index):
    ls = []
    try:
        for i in comments:
            if i['item_id'] == int(id) and i['index'] <= int(index):
                ls.append(i)
    except Exception as e:
        print(e)
    return ls

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='192.168.50.238')