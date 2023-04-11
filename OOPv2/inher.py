class NhanVien():
    def __init__(self, name, month , luong_co_ban, ngay_lam_viec, he_so_luong,hshq):
        self.name = name
        self.thang = month
        self.luong_co_ban = luong_co_ban
        self.he_so_luong = he_so_luong
        self.ngay_lam_viec = ngay_lam_viec
        self.hshq = hshq
        self.luong_thucnhan = 0


    def tinh_luong(self):
        self.luong_ct = (self.luong_co_ban * self.ngay_lam_viec * self.he_so_luong) - 1000000
        self.luong_nhan_ct  = self.luong_ct
        if self.luong_ct > 9000000:
            self.luong_nhan_ct = self.luong_ct * 0.9
        if self.hshq < 1:
            self.luong_thucnhan = self.luong_nhan_ct * self.hshq
        else:
            self.luong_thuong = self.luong_ct *(self.hshq - 1) * 0.85
            self.luong_thucnhan = self.luong_nhan_ct + self.luong_thuong
        
        return self.luong_thucnhan

    def hien_thi_luong(self):
        name = self.name
        thang = self.thang
        luong = int(self.tinh_luong())
        fluong = "{:,}".format(luong).replace(',','.')
        print(f"Luong cua nhan vien {name} han duoc trong thang {thang} la: {fluong}")

ten = input("Nhap ten nhan vien: ")   
thang = input("Nhap ten thang: ")   
luongcb = int(input("Nhap luong can ban: "))  
ngaycong = int(input("Nhap ngay cong: "))
hsl = float(input("nhap he so luong: "))
hshq = float(input("nhap he so hieu qua: "))
nv = NhanVien(ten, thang, luongcb, ngaycong, hsl, hshq)
nv.hien_thi_luong()