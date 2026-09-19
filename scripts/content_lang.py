# Language pages: Indonesian (id) + Roman Urdu (ur).
# Each is a localized tool page (merge / compress) with localized content.

LANG = {}

LANG["id/gabung-pdf"] = dict(
    tool="merge-pdf",
    lang="id",
    hreflang=[
        ("en", "https://www.pdfzaap.online/merge-pdf.html"),
        ("id", "https://www.pdfzaap.online/id/gabung-pdf.html"),
        ("ur", "https://www.pdfzaap.online/ur/pdf-merge-kaise-karein.html"),
        ("x-default", "https://www.pdfzaap.online/merge-pdf.html"),
    ],
    title="Gabung PDF Online Gratis — Satukan File PDF | PDFZaap",
    meta="Gabungkan beberapa PDF menjadi satu dokumen langsung di browser. Gratis, tanpa akun, tanpa watermark — file Anda tidak pernah diunggah.",
    h1="Gabung PDF — Gratis, Privat, Tanpa Akun",
    direct_answer="<p><strong>Jawaban cepat:</strong> Ya — Anda bisa menggabungkan (gabung) PDF sepenuhnya di browser. File dibaca dari perangkat Anda, digabung di memori browser, lalu hasilnya diunduh kembali ke perangkat Anda. Tidak ada langkah upload sama sekali.</p>",
    intro="<p>Butuh menyatukan beberapa file PDF — lamaran kerja, invoice, atau dokumen resmi — tanpa mengirim file ke server mana pun? Halaman ini menggabungkan alat gabung PDF yang berjalan sepenuhnya di browser dengan panduan singkat dalam bahasa Indonesia. Semua pemrosesan terjadi di perangkat Anda: tidak ada akun, tidak ada watermark, tidak ada batasan file.</p>",
    extra_sections="""<h2>Kenapa gabung PDF di browser lebih privat</h2>
<ul class="tips-list">
  <li><strong>Bukan diunggah ke server.</strong> File PDF Anda tidak pernah dikirim ke situs lain. Gabungan diproses di tab browser Anda.</li>
  <li><strong>Tidak ada batas harian.</strong> Karena tidak ada server yang memproses, tidak ada kuota atau batas penggunaan.</li>
  <li><strong>Hasil tanpa watermark.</strong> Dokumen gabungan tidak diberi tanda apa pun.</li>
</ul>
<p>Anda juga bisa memverifikasi sendiri bahwa tidak ada upload: buka DevTools browser (tekan F12), pilih tab Network, lalu jalankan alat dengan file uji. Tidak akan ada permintaan upload yang memuat file Anda. Panduan lengkapnya ada di <a href="/blog/how-to-check-if-pdf-tool-uploads-files.html">cara mengecek apakah tool PDF mengunggah file Anda</a>.</p>""",
    howto_title="menggabungkan file PDF",
    howto=[
        ("Tambahkan file PDF", "Klik area unggah dan pilih beberapa file PDF sekaligus. Urutan pilihan adalah urutan halaman hasil gabung."),
        ("Periksa urutan", "File tampil sesuai urutan pilihan. Hapus lalu pilih ulang jika urutan perlu diubah."),
        ("Klik 'Merge PDFs'", "Browser menyalin semua halaman dari semua file ke dalam satu dokumen baru."),
        ("Unduh PDF gabungan", "File hasil langsung tersimpan ke perangkat Anda."),
    ],
    why_title="menyatukan dokumen sensitif dengan aman",
    why="<p><strong>Kerahasiaan adalah alasannya.</strong> Dokumen yang biasa digabung — kontrak, invoice, salinan KTP, berkas lamaran — justru file yang paling tidak ingin Anda kirim ke server pihak lain. Karena pemrosesan terjadi di browser, file Anda tidak pernah menyeberangi jaringan.</p><p class='subtext'><strong>Hasil tanpa kehilangan kualitas.</strong> Penggabungan menyalin halaman asli apa adanya — tidak ada re-encoding, tidak ada penurunan kualitas, teks tetap bisa disalin. Jika file terenkripsi, buka dulu dengan <a href='/unlock-pdf.html'>Unlock PDF</a> (butuh kata sandi).</p>",
    tips=[
        "Beri nama file dengan awalan angka (01-, 02-, 03-) agar urutan gabung jelas.",
        "Setelah menggabungkan berkas besar, periksa jumlah halamannya di pembaca PDF sebelum dikirim.",
        "Jika hasil gabungan terlalu besar untuk diunggah ke portal, kecilkan dengan <a href='/compress-pdf.html'>Compress PDF</a> (mode target ukuran tersedia).",
        "Untuk memisahkan halaman dari dokumen gabungan, gunakan <a href='/split-pdf.html'>Split PDF</a>.",
    ],
    when="<p>Halaman ini untuk pencarian berbahasa Indonesia seperti 'gabung pdf', 'merge pdf online gratis', 'satuatukan pdf'. Alat-nya identik dengan halaman <a href='/merge-pdf.html'>Merge PDF</a> berbahasa Inggris. Untuk membalik proses (memecah PDF), gunakan <a href='/split-pdf.html'>Split PDF</a>; untuk memperkecil ukuran hasil, lihat <a href='/compress-pdf-to-200kb.html'>kompres PDF ke 200 KB</a> atau <a href='/compress-pdf-to-1mb.html'>kompres ke 1 MB</a>.</p>",
    faqs=[
        ("Apakah file saya diunggah ke server?", "Tidak. File dibaca oleh browser dari perangkat Anda, digabung di memori browser, dan hasilnya diunduh kembali ke perangkat Anda. Tidak ada langkah upload."),
        ("Berapa banyak file yang bisa digabung?", "Segala yang bisa ditampung memori browser Anda — tidak ada batas yang kami tetapkan."),
        ("Apakah kualitas dokumen berkurang?", "Tidak. Halaman disalin apa adanya, tanpa kompresi atau perubahan kualitas."),
        ("Apakah gratis dan tanpa akun?", "Ya. Semua alat di PDFZaap gratis, tanpa pendaftaran, tanpa watermark, tanpa batas harian."),
    ],
    related=[("split-pdf", "Split PDF"), ("compress-pdf", "Compress PDF"), ("reorder-pages-pdf", "Reorder Pages"), ("extract-pages-pdf", "Extract Pages")],
)

LANG["id/kompres-pdf"] = dict(
    tool="compress-pdf",
    lang="id",
    hreflang=[
        ("en", "https://www.pdfzaap.online/compress-pdf.html"),
        ("id", "https://www.pdfzaap.online/id/kompres-pdf.html"),
        ("ur", "https://www.pdfzaap.online/ur/pdf-compress-kaise-karein.html"),
        ("x-default", "https://www.pdfzaap.online/compress-pdf.html"),
    ],
    title="Kompres PDF Online Gratis — Kecilkan Ukuran File | PDFZaap",
    meta="Kompres PDF langsung di browser: pilih kualitas 0,1–1,0 atau target ukuran seperti 200 KB. File diproses lokal, tidak diunggah. Gratis, tanpa watermark.",
    h1="Kompres PDF — Gratis, di Browser Anda",
    direct_answer="<p><strong>Jawaban cepat:</strong> Kompres PDF gratis tanpa mengunggah file — pemrosesan terjadi di browser Anda. Pilih kualitas manual (0,1 sampai 1,0) atau target ukuran (misalnya di bawah 200 KB); alat akan mencari kualitas terbaik yang memenuhi batas, dan memberitahu Anda secara jujur jika batas tidak tercapai.</p>",
    intro="<p>File PDF yang terlalu besar sering menjadi masalah saat mengirim email atau mengunggah ke portal lamaran. Halaman ini menyediakan alat kompresi yang berjalan sepenuhnya di browser — dengan panduan dalam bahasa Indonesia. Anda bisa memilih kualitas secara manual, atau memilih target ukuran dan membiarkan alat mencari pengaturan terbaik. File tidak pernah meninggalkan perangkat Anda.</p>",
    extra_sections="""<h2>Kenapa ukuran PDF bisa terlalu besar</h2>
<ul class="tips-list">
  <li><strong>Scan resolusi tinggi</strong> — scan 300–600 dpi jauh lebih besar daripada scan 150 dpi untuk keperluan layar.</li>
  <li><strong>Gambar yang belum dikompres</strong> — foto beresolusi penuh dari ponsel adalah penyumbang terbesar.</li>
  <li><strong>Jumlah halaman banyak</strong> — dokumen puluhan halaman menumpuk ukuran halaman demi halaman.</li>
</ul>
<p>Panduan lengkapnya: <a href='/blog/why-is-my-pdf-file-so-large.html'>Kenapa file PDF saya begitu besar?</a> (berbahasa Inggris) dan artikel blog bahasa Indonesia <a href='/blog/kompres-pdf-online-gratis.html'>cara kompres PDF online gratis</a>.</p>
<h2>Catatan jujur tentang hasil kompresi</h2>
<p>Alat ini bekerja dengan merender ulang setiap halaman sebagai gambar JPEG. Ini sangat efektif untuk dokumen berbasis gambar (scan, laporan berfoto), tetapi teks dalam hasil <strong>tidak lagi bisa disalin</strong> — halamannya menjadi gambar. Jika penerima harus menyalin atau mencari teks di dokumennya, jangan kompres dengan cara ini; gunakan file aslinya.</p>""",
    howto_title="mengecilkan file PDF",
    howto=[
        ("Pilih file PDF", "Unggah dokumen yang perlu diperkecil."),
        ("Pilih mode", "Atur slider kualitas (0,1–1,0) secara manual, atau pilih target ukuran seperti 'Under 200 KB'."),
        ("Klik 'Compress PDF'", "Halaman dirender ulang secara lokal. Mode target mungkin butuh beberapa putaran untuk menemukan hasil terbaik."),
        ("Unduh dan baca catatan hasilnya", "Hasilnya menyertakan ukuran awal vs akhir — dan peringatan jujur jika kompresi tidak membantu."),
    ],
    why_title="memperkecil file tanpa mengunggahnya",
    why="<p><strong>Tanpa antrean, tanpa watermark.</strong> Alat kompresi berbasis upload menyimpan dokumen Anda di server mereka (sering dengan timer penghapusan yang harus Anda percaya). Di sini kompresi berjalan di memori browser Anda: file dibaca lokal, di-encode lokal, dan disimpan lokal. Tidak ada meteran, tidak ada tanda air di hasil.</p><p class='subtext'><strong>Batasan yang dijelaskan di depan.</strong> Karena halaman dirender ulang sebagai gambar, hasil kompresi tidak lagi memiliki teks yang bisa disalin. Untuk dokumen yang isinya harus bisa disalin, lebih baik perkecil dari sumbernya (export ulang dengan resolusi lebih rendah) daripada mengompres dengan alat ini.</p>",
    tips=[
        "Untuk portal lamaran yang membatasi 200 KB, gunakan mode target 200 KB — lihat juga halaman <a href='/compress-pdf-to-200kb.html'>kompres PDF ke 200 KB</a>.",
        "Kualitas 0,4–0,6 biasanya titik terbaik untuk lampiran email; turunkan lebih rendah hanya jika batasnya ketat.",
        "Jika catatan hasil menyatakan file sudah efisien, berarti isinya kebanyakan teks — kompresi render ulang tidak banyak membantu; pertimbangkan mengurangi halaman.",
        "Setelah mengompres, buka file untuk memastikan jumlah halaman sama dan dokumen terbaca normal.",
        "Untuk batas ukuran email, baca <a href='/blog/compress-pdf-for-email.html'>cara mengompres PDF untuk email (di bawah 2 MB)</a>.",
    ],
    when="<p>Gunakan halaman ini untuk memperkecil file PDF tanpa mengunggahnya. Untuk target ukuran tertentu: <a href='/compress-pdf-to-100kb.html'>100 KB</a>, <a href='/compress-pdf-to-200kb.html'>200 KB</a>, <a href='/compress-pdf-to-500kb.html'>500 KB</a>, <a href='/compress-pdf-to-1mb.html'>1 MB</a>, <a href='/compress-pdf-to-2mb.html'>2 MB</a>. Halaman alat utama berbahasa Inggris: <a href='/compress-pdf.html'>Compress PDF</a>. Artikel berbahasa Indonesia: <a href='/blog/kompres-pdf-online-gratis.html'>kompres PDF online gratis tanpa kehilangan kualitas</a>.</p>",
    faqs=[
        ("Apakah teks masih bisa disalin setelah kompresi?", "Tidak — halaman dirender ulang sebagai gambar. Jika penerima harus menyalin teks, gunakan file aslinya untuk keperluan itu."),
        ("Apa yang diubah oleh slider kualitas?", "Slider mengatur kualitas JPEG saat halaman di-encode ulang. Nilai lebih rendah = file lebih kecil, gambar lebih lembut. 0,6 adalah nilai seimbang."),
        ("Bagaimana jika target ukuran tidak tercapai?", "Alat memberitahunya secara jujur: ia menurunkan resolusi dan kualitas sejauh masih layak, lalu mengembalikan hasil terkecil yang mungkin dengan penjelasan alasannya."),
        ("Apakah ada batas ukuran file?", "Tidak ada batas yang kami tetapkan. File sangat besar membutuhkan memori dan waktu browser lebih lama karena semua pemrosesan terjadi lokal."),
    ],
    related=[("merge-pdf", "Merge PDF"), ("split-pdf", "Split PDF"), ("jpg-to-pdf", "JPG to PDF"), ("compress-pdf", "Compress PDF (EN)")],
)

LANG["ur/pdf-compress-kaise-karein"] = dict(
    tool="compress-pdf",
    lang="ur-Latn",
    hreflang=[
        ("en", "https://www.pdfzaap.online/compress-pdf.html"),
        ("id", "https://www.pdfzaap.online/id/kompres-pdf.html"),
        ("ur", "https://www.pdfzaap.online/ur/pdf-compress-kaise-karein.html"),
        ("x-default", "https://www.pdfzaap.online/compress-pdf.html"),
    ],
    title="PDF Compress Kaise Karein — Free, Bina Upload | PDFZaap",
    meta="PDF compress kaise karein bina upload kiye — mukammal kaam aap ke browser mein. Free, bina signup, target size (200KB, 1MB) choose karein.",
    h1="PDF Compress Kaise Karein — Free aur Private",
    direct_answer="<p><strong>Seedha jawab:</strong> PDF compress karna ab upload ke bina bhi mumkin hai. Yeh tool aap ke browser ke andar chalta hai — file aap ke device se padhi jaati hai, wahan hi compress hoti hai, aur result aap ke device par download hota hai. Koi upload step hi nahi hota.</p>",
    intro="<p>PDF file ka size chota karna aksar zaroori hota hai — job portal ki limit, email ka attachment cap, ya kisi form ki requirement. Yeh page sikhata hai ke PDF compress kaise karein bina usay kisi server par bheja, ek free tool ke sath jo mukammal tarah se aap ke browser mein chalta hai. Aap quality manually set kar sakte hain ya target size chun sakte hain (masalan 200 KB ya 1 MB ke neeche), aur tool behtareen quality khud dhundh leta hai.</p>",
    extra_sections="""<h2>PDF compress karna kyun zaroori hota hai</h2>
<ul class="tips-list">
  <li><strong>Job portals</strong> — kai application forms mein CV ka size 200 KB ya 500 KB se zyada nahi hona chahiye.</li>
  <li><strong>Email limits</strong> — purani corporate aur government email systems ke attachment caps chote hote hain.</li>
  <li><strong>University applications</strong> — transcripts aur documents ki per-file limits aam hain.</li>
</ul>
<p>Detail ke sath guide: <a href='/blog/compress-pdf-under-200kb-job-application.html'>job application ke liye PDF ko 200 KB se neeche kaise karein</a> aur <a href='/blog/how-to-make-pdf-smaller-without-adobe.html'>Adobe ke bina PDF choti kaise karein</a> (English mein).</p>
<h2>Result ke baare mein seedhi baat</h2>
<p>Yeh tool har page ko dobara image (JPEG) ke taur par render kar ke PDF banata hai. Image-heavy documents (scans, photos) par yeh kaam bahut asar daalta hai, lekin result mein text copy nahi ho sakta — pages images ban jaati hain. Agar document ka text copy karna zaroori hai, toh us ke liye original file use karein.</p>""",
    howto_title="PDF compress karne ke steps",
    howto=[
        ("PDF file select karein", "Dropzone par click kar ke woh file chunein jise chota karna hai."),
        ("Mode choose karein", "Quality slider (0.1 se 1.0) manually set karein, ya target size jaise 'Under 200 KB' chunein."),
        ("'Compress PDF' par click karein", "Pages aap ke browser mein hi dobara encode hoti hain. Target mode mein tool behtareen fit ke liye kuch passes leta hai."),
        ("Download karein aur note parhein", "Result mein original aur naya size dono likha hota hai — agar compression kaam na kare, toh woh wahan likha hoga."),
    ],
    why_title="upload ke bina file chhoti karein",
    why="<p><strong>Privacy ka faayda.</strong> Upload-based compression services aap ke document ko apne servers par rakhti hain. Yahan mukammal kaam aap ke browser ke memory mein hota hai — file kabhi network se nahi guzarti. Na koi meter, na koi watermark, na koi account.</p><p class='subtext'><strong>Bataye hue limits.</strong> Kyunki pages dobara images banayi jaati hain, compressed file mein text selectable nahi rehta. Text-critical documents ke liye source se dobara export karna (chhoti resolution par) behtar hai — is baat ko hum seedha likhte hain.</p>",
    tips=[
        "Job portal ki 200 KB limit ke liye target mode mein 200 KB chunein — <a href='/compress-pdf-to-200kb.html'>200 KB guide</a> bhi parhein.",
        "Quality 0.4 se 0.6 email attachments ke liye aam taur par behtareen hota hai.",
        "Agar result note bataye ke file pehle se efficient thi, toh usay chora hue original file use karein.",
        "Email limits ke liye 2 MB target sab se aam hai: <a href='/compress-pdf-to-2mb.html'>2 MB guide</a>.",
    ],
    when="<p>Yeh page 'pdf compress kaise karein' jaise Roman Urdu queries ke liye hai. Tools ki English pages: <a href='/compress-pdf.html'>Compress PDF</a>, aur size-specific guides: <a href='/compress-pdf-to-100kb.html'>100 KB</a>, <a href='/compress-pdf-to-200kb.html'>200 KB</a>, <a href='/compress-pdf-to-500kb.html'>500 KB</a>, <a href='/compress-pdf-to-1mb.html'>1 MB</a>, <a href='/compress-pdf-to-2mb.html'>2 MB</a>. Files chhota karna ho toh pehle <a href='/blog/why-is-my-pdf-file-so-large.html'>yeh samjhain ke PDF itna bada kyun hai</a>.</p>",
    faqs=[
        ("Kya file kisi server par upload hoti hai?", "Nahi. File aap ke browser se device par padhi jaati hai, browser ke memory mein compress hoti hai, aur download ke taur par wapas aap ke device par likhi jaati hai."),
        ("Compress ke baad text copy hota hai?", "Nahi — pages images ke taur par render hoti hain. Text copy karne ke kaam ke liye original file use karein."),
        ("Target size nahi mila toh kya hoga?", "Tool bech rahe sab se chhota result de deta hai aur seedha batata hai ke target kyun nahi mila — koi jhoot ka 'success' nahi."),
        ("Kya yeh mobile par bhi chalta hai?", "Haan — phone ke browser mein bhi mukammal processing local hoti hai. Bahut badi files par desktop tez ho sakta hai."),
    ],
    related=[("compress-pdf", "Compress PDF (EN)"), ("split-pdf", "Split PDF"), ("merge-pdf", "Merge PDF"), ("jpg-to-pdf", "JPG to PDF")],
)

LANG["ur/pdf-merge-kaise-karein"] = dict(
    tool="merge-pdf",
    lang="ur-Latn",
    hreflang=[
        ("en", "https://www.pdfzaap.online/merge-pdf.html"),
        ("id", "https://www.pdfzaap.online/id/gabung-pdf.html"),
        ("ur", "https://www.pdfzaap.online/ur/pdf-merge-kaise-karein.html"),
        ("x-default", "https://www.pdfzaap.online/merge-pdf.html"),
    ],
    title="PDF Merge Kaise Karein — Free, Bina Upload | PDFZaap",
    meta="PDF merge kaise karein bina upload — kai PDF files ko ek document mein joren, kaam aap ke browser mein. Free, bina signup, file device se nahi nikalti.",
    h1="PDF Merge Kaise Karein — Free aur Private",
    direct_answer="<p><strong>Seedha jawab:</strong> Haan — aap kai PDF files ko ek document mein jod sakte hain bina unhein kisi server par bheja. Tool aap ke browser mein chalta hai: files aap ke device se padhi jaati hain, memory mein merge hoti hain, aur combined file aap ke device par download hoti hai.</p>",
    intro="<p>PDF merge karna aam zaroorat hai — CV ke saath cover letter, invoices ka bundle, ya application ke documents. Yeh page sikhata hai ke PDF merge kaise karein bina upload kiye, ek free tool ke sath jo browser ke andar chalta hai. Koi account nahi, koi watermark nahi, koi daily limit nahi — aur aap ke files hamesha aap ke device par rehte hain.</p>",
    extra_sections="""<h2>Bina upload merge kyun behtar hai</h2>
<ul class="tips-list">
  <li><strong>Files kahin nahi jaati.</strong> Aap ka document kisi third-party server par na toh upload hota hai aur na toh store. Privacy ka sawal hi khatam ho jaata hai.</li>
  <li><strong>Na meter, na limit.</strong> Kyunki server kaam nahi karta, aap jitni files chahein merge kar sakte hain.</li>
  <li><strong>Quality bhi aisi hi rehti hai.</strong> Merge pages ko aisi hi copy karta hai jaise woh hain — koi re-encoding nahi, koi quality loss nahi.</li>
</ul>
<p>Aap khud verify bhi kar sakte hain ke upload nahi ho raha: DevTools kholen (F12), Network tab par jayen, aur tool chalayein — aap ki file kisi request mein nahi dikhegi. Pura guide: <a href='/blog/how-to-check-if-pdf-tool-uploads-files.html'>check kaise karein ke koi PDF tool files upload karta hai</a> (English mein).</p>""",
    howto_title="PDF merge karne ke steps",
    howto=[
        ("PDF files add karein", "Dropzone par click kar ke jitni files chahein select karein. Selection ki order hi merge ki order hogi."),
        ("Order check karein", "Files list mein selection ki order mein dikhti hain. Kisi ko hilana ho toh remove kar ke dobara add karein."),
        ("'Merge PDFs' par click karein", "Browser har file ke saare pages ko ek naye document mein copy karta hai."),
        ("Combined PDF download karein", "Tayyar file seedha aap ke device par save hoti hai."),
    ],
    why_title="sensitive documents ko safe rakhein",
    why="<p><strong>Woh files jo aap protect karna chahte hain.</strong> Contracts, invoices, ID ke scans, HR ke records — yeh woh documents hain jo aap kisi aur ke server par nahi chahte. Client-side merge yeh risk hata deta hai: site par koi upload endpoint hi nahi hai.</p><p class='subtext'><strong>Seedhi baat limits par.</strong> Bahut badi batches browser ki memory use karte hain, aur encrypted files pehle <a href='/unlock-pdf.html'>Unlock PDF</a> se khulti hain (password zaroori). Yeh same limits hain jo kisi bhi local PDF operation ko hote hain.</p>",
    tips=[
        "Files ko 01-, 02-, 03- se number dein taake order saaf rahe.",
        "Merge ke baad pages ki ginti check karein — total inputs ke pages ke barabar honi chahiye.",
        "Agar combined file kisi portal ki size limit se badi hai, toh <a href='/compress-pdf.html'>Compress PDF</a> se chhoti karein — pehle merge, phir compress.",
        "Pages alag karni hon toh <a href='/split-pdf.html'>Split PDF</a> use karein.",
        "Mobile par bhi yehi local model chalta hai — <a href='/blog/how-to-merge-pdf-files-on-iphone.html'>iPhone par merge karne ka guide</a> parhein.",
    ],
    when="<p>Yeh page 'pdf merge kaise karein' aur 'merge pdf bina upload kiye' jaise queries ke liye hai. Tool English page se mukammal same hai: <a href='/merge-pdf.html'>Merge PDF</a>. Size limits ke liye: <a href='/compress-pdf-to-200kb.html'>200 KB</a> aur <a href='/compress-pdf-to-1mb.html'>1 MB</a> guides. Privacy ka poora masla: <a href='/is-it-safe-to-use-online-pdf-tools.html'>online PDF tools safe hain kaise?</a></p>",
    faqs=[
        ("Kya meri files device se bahar jaati hain?", "Nahi. Browser files ko disk se padhta hai, merge aap ke tab ke memory mein hota hai, aur download result ko wapas aap ke device par likhta hai. Document ka koi network path hi nahi hai."),
        ("Kya offline bhi chalta hai?", "Haan — page load ho jane ke baad merge ke liye internet ki zaroorat nahi. Yehi is baat ki sab se aasan proof hai ke processing aap ke device par hoti hai."),
        ("Quality kam nahi hoti?", "Nahi — pages structural copy hote hain, re-render nahi hote. Na compression, na watermark."),
        ("Kitni files merge kar sakti hoon?", "Jo aap ke browser ki memory mein fit ho — hum koi limit nahi lagate."),
    ],
    related=[("merge-pdf", "Merge PDF (EN)"), ("split-pdf", "Split PDF"), ("compress-pdf", "Compress PDF"), ("protect-pdf", "Protect PDF")],
)
