class Place:
    def __init__(self, no, name_kor, name_eng, translated_name_eng, address, lat, lng, created_at, last_searched_at):
        self.no = no
        self.name_kor = name_kor
        self.name_eng = name_eng
        self.translated_name_eng = translated_name_eng
        self.address = address
        self.lat = lat
        self.lng = lng
        self.created_at = created_at
        self.last_searched_at = last_searched_at