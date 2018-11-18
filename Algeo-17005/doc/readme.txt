Cara menjalankan program dengan interpreter:
  1. Pastikan python terinstall dengan versi >=3.6
  2. Pastikan library PyOpenGL terinstall sesuai dengan sistem operasi. Pada sistem operasi windows gunakan binary unofficial
  3. Navigasikan terminal ke folder 'src'
  4. Interpret file 'main.py' dengan perintah 'python main.py'

Cara menjalankan program dengan compiled binary:
  1. Navigasikan terminal ke folder 'bin'
  2. Ubah binary main menjadi executable dengan perintah 'chmod +x main'
  3. Jalankan file 'main' dengan perintah './main'

Penggunaan:
  [DUA DIMENSI]
  translate <dx> <dy>	    : Translasi objek sebesar dx pada sumbu x dan dy pada sumbu y
  dilate <k>		          : Dilatasi objek dengan skala k
  rotate <deg> <a> <b>	  : Rotasi objek berlawanan arah jarum jam (CCW) sebesar deg terhadap titik a,b
  reflect <param>		      : Pencerminan objek terhadap sumbu atau titik a,b pada parameter
                          Parameter valid : x | y | x=y | x=-y | (<a>,<b>)
  shear <x|y> <k>		      : Shear pada objek dengan skala k, relatif terhadap sumbu x atau y
  stretch <x|y> <k>	      : Stretch pada objek dengan skala k, relatif terhadap sumbu x atau y
  custom <a> <b> <c> <d>	: Transformasi linier pada objek dengan matriks transformasi berikut
                          |a b|
                          |c d|
  color                   : Recolor objek

  [TIGA DIMENSI]
  translate <dx> <dy> <dz>
  dilate <k>
  rotate <deg> <a> <b> <c>
  reflect <xy | yz | xz | (<a>,<b>,<c>)>
  shear <x | y | z | xy | yz | xz> <k> [<k2>]
  stretch <x|y|z> <k>
  custom <a b c d e f g h i>

  [UMUM]
  multiple <n>		     : Melakukan transformasi linear pada objek sebanyak n kali secara berurutan
  reset			           : Mengembalikan objek ke kondisi awal
  exit			           : Exit program
