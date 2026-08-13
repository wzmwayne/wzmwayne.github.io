// 链接列表（单独维护文件）：修改链接只需编辑本文件
//
// 结构约定：
//   值 = 字符串 URL            -> 链接按钮
//   值 = "[text]文字"          -> 文字组件（[text] 后的内容为显示文字，效果设置预留扩展）
//   值 = 对象（含嵌套）        -> 嵌套分组
//   每个分组对象可含 "setting" 子字典：
//       collapsed    : true 默认折叠该组，false 默认展开
//       collapsible  : false 禁止折叠该组（其余键预留扩展）
var categories = {
    "快链接（仅提供链接，不承担任何责任）": {
        "setting": { "collapsed": true },
        "老豆荚旧版": "https://oldpods.mysxl.cn/old",
        "“新月的摇篮曲”歌曲下载": "https://ghproxy.net/github.com/wzmwayne/wzmwayne.github.io/releases/download/data/HOYO-MiX.-.Lullaby.of.the.New.Moon.I.Somnias.a.Luna.mp3",
        "读日月前事（并非整活）": "https://whdn.lanzouu.com/iyxXS3qrtvtg",
        "番茄小说简版": "https://whdn.lanzouu.com/iKRP1427pd4b",
        "下载轻松签": "https://xiaobai51.top",
        "下载flclash": "https://pan.huang1111.cn/s/jR3KDuy",
        "下载chrome旧版(edgeone)": "https://edgeone.gh-proxy.org/https://github.com/wzmwayne/wzmwayne.github.io/releases/download/data/4.4.Chrome_80.0.3987.149.apk",
        "下载chrome旧版(fastly)": "https://cdn.gh-proxy.org/https://github.com/wzmwayne/wzmwayne.github.io/releases/download/data/4.4.Chrome_80.0.3987.149.apk",
        "下载mt管理器(官网)": "https://mt2.cn/download/",
        "下载白名单管理器（即将开源）(fastly)": "https://cdn.gh-proxy.org/https://github.com/wzmwayne/wzmwayne.github.io/releases/download/data/whitelist.apk",
        "下载白名单管理器（即将开源）(edgeone)": "https://edgeone.gh-proxy.org/https://github.com/wzmwayne/wzmwayne.github.io/releases/download/data/whitelist.apk",
        "站长提示": "[text]以上下载链接仅供学习交流使用，请自行判断安全性，本人不承担任何责任"
    },
    "较大项目": {
        "setting": { "collapsed": false },
        "BetterSeewo 系列": {
            "下载 BetterSeewo": "https://wzml.cc.cd/betterseewo/",
            "下载 锁屏工具": "https://github.com/wzmwayne/locker/releases/download/1.0/default.exe",
            "锁屏介绍": "https://github.com/wzmwayne/locker/releases/tag/1.0"
        },
        "其他项目": {
            "setting": { "collapsed": true },
            "iFlow API": "https://wzml.cc.cd/iflow-api/#",
            "touchtools": "https://wzml.cc.cd/WPPtools/"
        }
    },
    "在线工具": {
        "Online CMD": "https://wzml.cc.cd/onlin_cmd/",
        "增加文件大小": "https://wzml.cc.cd/Increase_File_Size/",
        "PrintHelper在线灵蝶版": "https://wzml.cc.cd/print_helper/",
        "github加速": "https://wzml.cc.cd/ghp",
        "教你 Bing 搜索": "https://wzmwayne.github.io/bing-search-tutorial/"
    },
    "游戏与启动": {
        "MC Lunch": "https://wzml.cc.cd/mclunch/"
    },
    "篡改猴脚本": {
        "ScriptWeaver灵蝶": "https://wzml.cc.cd/ScriptWeaver/"
    },
    "社交与其它": {
        "setting": { "collapsed": false },
        "我的哔哩哔哩(已封号)": "https://space.bilibili.com/3546822289131703",
        "Free VPN (Clash) ": "https://ghproxy.net/github.com/Au1rxx/free-vpn-subscriptions/raw/main/output/clash.yaml",
        "webd网盘": "https://wzml.cc.cd/github-webd/"
    }
};
