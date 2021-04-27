# -*- coding: utf-8 -*-

# Scrapy settings for Matchfashion_title project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Matchfashion_title'

SPIDER_MODULES = ['Matchfashion_title.spiders']
NEWSPIDER_MODULE = 'Matchfashion_title.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Matchfashion_title (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Matchfashion_title.middlewares.MatchfashionTitleSpiderMiddleware': 543,
#}
cookies = {
    'SESSION_TID': 'KN5IF8MQBQFJ4-162Q89C',
    'plpLayoutMobile': '2',
    'plpLayoutTablet': '2',
    'plpLayoutDesktop': '3',
    'plpLayoutLargeDesktop': '4',
    '_pxhd': '57ac91f543bc2cef9fb31f2926308fa0e9dd4404e54aa5c2d422c7b5019a37ad:72bb27c1-9620-11eb-8608-ab1294d54075',
    'ab-user-id': '81',
    '_dy_c_exps': '',
    '_gcl_au': '1.1.578330312.1617635195',
    '_ga': 'GA1.2.1049601072.1617635195',
    '_gid': 'GA1.2.533570201.1617635195',
    '_dycnst': 'dg',
    '_dyid': '-4485584286645540989',
    '_dycst': 'dk.w.c.ms.',
    'country': 'CHN',
    'billingCurrency': 'USD',
    'indicativeCurrency': 'CNY',
    'saleRegion': 'APAC',
    '_dyid_server': '-4485584286645540989',
    'rskxRunCookie': '0',
    'rCookie': 'ydvpn017tpmtp7rnq87m3kn4q8xt5',
    '_cs_c': '0',
    '_pxvid': '72bb27c1-9620-11eb-8608-ab1294d54075',
    'sizeTaxonomy': '',
    'gender': 'mens',
    '_dy_c_att_exps': '',
    '_fbp': 'fb.1.1617635285889.1847561044',
    '_pin_unauth': 'dWlkPU9UZGlPR1V5TW1RdE5XTmtZUzAwWWpoakxUaGxOMkV0T0RKa01XSTVPV1JtWVRaaQ',
    '_dy_csc_ses': 't',
    '_dyjsession': '29f1e24fb4a8406c8106d1182bf33efa',
    'dy_fs_page': 'www.matchesfashion.com%2Fintl%2Fmens%2Fshop%2Fclothing%3Fpage%3D1%26noofrecordsperpage%3D240%26sort%3D',
    '_dy_geo': 'JP.AS.JP_13.JP_13_Tokyo',
    '_dy_df_geo': 'Japan..Tokyo',
    'AMCVS_62C33A485B0EB69A0A495D19%40AdobeOrg': '1',
    'AMCV_62C33A485B0EB69A0A495D19%40AdobeOrg': '-1124106680%7CMCIDTS%7C18723%7CMCMID%7C64545836408127940140713904933429812675%7CMCAAMLH-1618287354%7C11%7CMCAAMB-1618287354%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1617689754s%7CNONE%7CMCSYNCSOP%7C411-18730%7CvVersion%7C5.2.0%7CMCCIDH%7C643491003',
    's_cc': 'true',
    'JSESSIONID': 's3~74025AE116899259DDCFE7206FCC10FA',
    '_gat_gtag_UA_4623109_1': '1',
    '_gat_ga_launch': '1',
    'language': 'en',
    'defaultSizeTaxonomy': 'MENSSHOESEUITSEARCH',
    'loginTracking': 'true',
    '_pxff_fp': '1',
    'mfstorefrontRememberMe': 'x+EOlq6Y0SWpTmWo+zGRPwBLE+W+VmbCxp8id28gbOVvvP2tbfFzjmmY9+jP/pxU2ISfcstKrsWzdOuVB5VfxjIc0KzCYCqIr2+FVQt5oqCqCs9GJEvT/IyKO6gzh50WgkFJxXgNexTTjwH+Oa8R/CFq4RAWAulTDoKjc6KMiqsvNTb8zTFxIMF9rPAQoLESgTMqIzLgxlhZTNfCpw+sdA==',
    'acceleratorSecureGUID': 'f62c045f94c8de9b34e8b8e4aa669f4ba4c55fc5',
    'userID': '2284058726@qq.com',
    'access_token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InByZHNramxra25oYmhxbCJ9.eyJ1aWQiOiIyMjg0MDU4NzI2QHFxLmNvbSIsInJvbGVzIjpbIlJPTEVfQ1VTVE9NRVJHUk9VUCJdLCJleHAiOjE2MTc2ODUyMTcsImNpZCI6IkM2NzAwNjkyIn0.gxj0mSes9JWX3R-KDGRI7uqZD8Q8KqrB73wGc_qcLNZDxZgrjPvR0JJ6CjqOtEBVneOh4IzknYValD7vo4_nuQK9XCshkEsSZfUvXrMR_k0K_7Y1nEX6q-PQumfIZtMPI_lFRNy1nRKRDdE0exnqwLEhzq7PIRrWEMvmuDJrNxhF-WF4rEC-nKSXOPNc8U61rR-9ux7lQgJQ2bOV15yuH_YGWja1sMmFQOjyAEpySZ2k3L3iTIiOU_Qqun_UvJ6_snPIH1M_6ZfgyyWc87nhTmfJbj4O3BziIcTdgkwOrhMaUgQt4DtRcye8Nb-FpPeGmx1GAX8QsMYO7uLYA1wayA',
    '_dy_ses_load_seq': '13249%3A1617683416371',
    '_dy_soct': '1003595.1005104.1617682550*1011332.1019298.1617683416*1047613.1113204.1617683416*1001485.1001871.1617683416',
    'gpv_pn': 'mens%3Ashop%3Aclothing',
    'loggedIn': 'true',
    '_dy_lu_ses': '29f1e24fb4a8406c8106d1182bf33efa%3A1617683417986',
    '_dy_toffset': '0',
    '_dd_s': 'rum=0&expire=1617684319991',
    's_sq': '%5B%5BB%5D%5D',
    'sailthru_pageviews': '7',
    '_uetsid': '9abe02a0962011eba590915927c73599',
    '_uetvid': '9abf07f0962011eb95394db8b5679600',
    '_cs_id': 'cec08ac3-fab1-a589-95ac-ec69e657d099.1617635228.2.1617683420.1617682563.1.1651799228643.Lax.0',
    '_cs_s': '7.1',
    'lastRskxRun': '1617683420646',
    'AWSALB': 'sfU604aWjb/IKMh335SpQcx/zf7Ll05mDlODip3tBz6kvLwMC+izi0ByqNPqCAJqoCV9SYvfz0ZFB50/9aXHkvgG+DtYYOBywj0wU7GCdy+JRQq7SQg8P0iDQxIm',
    'AWSALBCORS': 'sfU604aWjb/IKMh335SpQcx/zf7Ll05mDlODip3tBz6kvLwMC+izi0ByqNPqCAJqoCV9SYvfz0ZFB50/9aXHkvgG+DtYYOBywj0wU7GCdy+JRQq7SQg8P0iDQxIm',
    '_px2': 'eyJ1IjoiY2JiNmJkNjAtOTY5MC0xMWViLWJlOTgtZWI5YjYwYWIzM2EzIiwidiI6IjcyYmIyN2MxLTk2MjAtMTFlYi04NjA4LWFiMTI5NGQ1NDA3NSIsInQiOjE2MTc2ODM5MjMyNDksImgiOiIxNzFkZTZhMmRkM2MxN2Q1ZGRkNWM2MzRiZjc5MWQ1ZjhjZGJhOTAwYzhmYTUzZTJjNWQwNmFjYWY4MTk2MmU4In0=',
    'sailthru_content': '11cc2b52e9ea4f9e19496de4ad0ba14ca82da1a1920b029368fc15e4de11cb05',
    'sailthru_visitor': '59f704de-6600-477a-9fa0-2d3a628a09d0',
}


DEFAULT_REQUEST_HEADERS = {
    'authority': 'www.matchesfashion.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'Referer': 'http://www.google.com',
    'accept-language': 'zh-CN,zh;q=0.9',
}
# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Matchfashion_title.middlewares.MatchfashionTitleDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'Matchfashion_title.pipelines.MatchfashionTitlePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
