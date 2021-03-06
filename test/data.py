#encoding: utf8

def theirsmessage(**kwargs):
    return dict(
        fromusername="they",
        tousername="me",
        createtime=1457600000,
        **kwargs
    )

def minemessage(**kwargs):
    return dict(
        fromusername="me",
        tousername="they",
        createtime=1457600000,
        **kwargs
    )
    
data = dict(
    event_subscribe=theirsmessage(
        msgtype="event",
        event="subscribe"
    ),
    event_barcode=theirsmessage(
        msgtype="event",
        event="SCAN",
        eventkey="scene_value",
        ticket="ticket"
    ),
    event_view=theirsmessage(
        msgtype="event",
        event="VIEW",
        eventkey="www.xavier-lam.com",
    ),
    event_click=theirsmessage(
        msgtype="event",
        event="CLICK",
        eventkey="EVENTKEY",
    ),
    message_text=theirsmessage(
        msgtype="text",
        content="中文",
        msgid=12345,
    ),
    message_pic=theirsmessage(
        msgtype="image",
        picurl="http://wechat.xavier-lam.com/example.jpg",
        msgid=12345,
        mediaid="123456",
    ),
    message_voice=theirsmessage(
        msgtype="voice",
        format="arm",
        msgid=12345,
        mediaid="123456",
    ),
    message_voice_with_rec=theirsmessage(
        msgtype="voice",
        format="arm",
        recognition="我嘞个去",
        msgid=12345,
        mediaid="123456",
    ),
    message_video=theirsmessage(
        msgtype="video",
        thumbmediaid="asdfds",
        msgid=12345,
        mediaid="sadsasdf",
    ),
    message_shortvideo=theirsmessage(
        msgtype="shortvideo",
        thumbmediaid="asdfds",
        msgid=12345,
        mediaid="sadsasdf",
    ),
    message_location=theirsmessage(
        msgtype="location",
        location_x=123.12,
        location_y=321.32,
        scale=12,
        label="851大楼",
        msgid=24435345
    ),
    message_url=theirsmessage(
        msgtype="link",
        title="标题",
        description="概述",
        url="http://www.xavier-lam.com/",
        msgid=1232131
    ),
)

mine=dict(
    message_text=minemessage(
        msgtype="text",
        content="卧槽",
    ),
    message_image=minemessage(
        msgtype="image",
        image=dict(
            mediaid="2111"
        )
    ),
    message_video=minemessage(
        msgtype="video",
        video=dict(
            mediaid="1221",
            title="标题",
            description="描述"
        )
    ),
    message_article=minemessage(
        msgtype="article",
        articlecount=2,
        articles=[{
            "title": "title1",
            "description": "description",
            "picurl": "picurl",
            "url": "url",
        }, {
            "title": "title2",
            "description": "description",
            "picurl": "picurl",
            "url": "url",
        }]
    )
)