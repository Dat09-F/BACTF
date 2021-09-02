# BACTF - FOR - WU

# Infinity Zip

Problem: Here's a zip, there's a zip. Zip zip everywhere.
File : flag.zip ( sau 1 lần extract thì mình đc file 999.zip )

Solution : Cần giải nén nốt 1000 file zip nén lồng nhau trong file 999.zip
Sử dụng py code để extract ( Extract Zip.py )

Sau khi giải nén mình nhận đc 1 file flag(FAKE).png nha

![alt text](https://github.com/Dat09-F/BACTF/blob/d2dc0ab22c892f5dff2b74ce4d19a3d870acfc90/Infinity%20Zip%20-%20flag(FAKE).png)

Cần strings đọc text trong ảnh. Và ra đc flag real! ( flag(REAL).png )

![alt text](https://github.com/Dat09-F/BACTF/blob/d2dc0ab22c892f5dff2b74ce4d19a3d870acfc90/Infinity%20Zip%20-%20flag(REAL).png)


# Zstegosaurus

Problem: My friend forgot our pet zstegosaurus's name. Luckily for him, I hid the dinosaur's name somewhere in this picture...but now I can't find it. Can you help us?
File : zstegosaurus.png

![alt text](https://github.com/Dat09-F/BACTF/blob/d2dc0ab22c892f5dff2b74ce4d19a3d870acfc90/zstegosaurus.png)

Solution:
Áp dụng tool đọc dữ liệu nâng cao cho riêng file png là zsteg ( ae tham khảo install ở đây https://github.com/zed-0xff/zsteg )
Trong terminal nhập zsteg zstegosaurus.png sẽ ra đc flag

![alt text](https://github.com/Dat09-F/BACTF/blob/d2dc0ab22c892f5dff2b74ce4d19a3d870acfc90/zstegosaurus%20-%20flag.png)

# Secure Zip

Problem: Gerald lost his homework in this zip file. He needs to extract his homework or else he fails CTF101.
File : chall.zip


Solution: 
Ae thấy file này bị nén pass, nhưng ko có key, mình sẽ dò key từ 1 file thư viện là rookyou.txt(https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)
Xài tool fcrackzip ( ae tham khảo install trên web nha )
Lệnh mình chụp trong image ( Secure Zip.png ) : -v kiểm tra thuật toán, -D sử dụng thư viện rookyou.txt, -u: loại trừ pass sai, -p: chọn ký tự trùng với pass ban đầu

![alt text](https://github.com/Dat09-F/BACTF/blob/d2dc0ab22c892f5dff2b74ce4d19a3d870acfc90/Secure%20Zip.png)

extract file chall.zip ta đc flag (Secure Zip-flag.png )

![alt text](https://github.com/Dat09-F/BACTF/blob/d2dc0ab22c892f5dff2b74ce4d19a3d870acfc90/zstegosaurus%20-%20flag.png)
