# Parsing 시 함께 오는 html 태그 제거

class stringCleaner:
    @staticmethod
    def clean(txt):
        txt = txt.replace("&lt;b&gt;", "")
        txt = txt.replace("<b>", "")
        txt = txt.replace("</b>", "")
        txt = txt.replace("&quot;", "")
        txt = txt.replace("", "")
        return txt
