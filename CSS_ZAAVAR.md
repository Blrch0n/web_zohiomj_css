# Өөрийн HTML файлуудыг CSS ашиглан шинэчлэх зааварчилгаа

## 1-р алхам: Хуудасны толгой үүсгэх

Та өөрийн HTML файл бүрийн эхэнд дараах бүтцийг хуул:

```html
<!DOCTYPE html>
<html lang="mn">
<head>
<meta charset="UTF-8">
<title>Хуудасны нэр</title>
<link rel="stylesheet" href="../styles/main.css">  <!-- member folder бол -->
<!-- эсвэл -->
<link rel="stylesheet" href="styles/main.css">  <!-- үндсэн файл бол -->
</head>
<body>
<div class="container">

<!-- Толгой хэсэг -->
<header class="header fade-in">
<div class="header-content">
<div class="logo-section">
<img src="../images/logo.png" alt="Лого">  <!-- member folder-т -->
<div class="title-section">
<h1>Онлайн сургалтын систем</h1>
<p>Боловсрол бол ирээдүй</p>
</div>
</div>
<div class="contact-info">
<div><strong>Утас:</strong> 77001122</div>
<div><strong>Імэйл:</strong> info@edu.mn</div>
</div>
</div>
</header>

<!-- Навигаци -->
<nav class="navigation">
<ul class="nav-menu">
<li><a href="../index.html">Нүүр хуудас</a></li>  <!-- member folder-т ../ нэм -->
<li><a href="../member1/courses.html">Хичээлүүд</a></li>
<li><a href="../member2/dashboard.html">Хянах самбар</a></li>
<li><a href="../member4/library.html">Номын сан</a></li>
<li><a href="../member5/exams.html">Шалгалт</a></li>
<li><a href="../member6/contact.html">Холбоо барих</a></li>
<li class="login-btn"><a href="../login.html">Нэвтрэх</a></li>
</ul>
</nav>

<!-- Үндсэн агуулга -->
<main class="main-content fade-in">
<div class="page-title">
<h2>Хуудасны Гарчиг</h2>
</div>
```

## 2-р алхам: Өөрийн агуулга нэмэх

Хуучин TABLE-уудаа дараах CLASS-уудаар солих:

### Хүснэгт мэдээлэл:
```html
<div class="data-table">
<table>
<tr>
<th>Толгой 1</th>
<th>Толгой 2</th>
</tr>
<tr>
<td>Өгөгдөл 1</td>
<td>Өгөгдөл 2</td>
</tr>
</table>
</div>
```

### Картууд (3 багана):
```html
<div class="cards-container">
<div class="card">
<div class="card-header">Гарчиг 1</div>
<div class="card-body">
<p>Агуулга...</p>
</div>
</div>

<div class="card">
<div class="card-header">Гарчиг 2</div>
<div class="card-body">
<p>Агуулга...</p>
</div>
</div>

<div class="card">
<div class="card-header">Гарчиг 3</div>
<div class="card-body">
<p>Агуулга...</p>
</div>
</div>
</div>
```

### Маягт (Form):
```html
<div class="form-container">
<form>
<div class="form-group">
<label>Нэр:</label>
<input type="text" name="name">
</div>

<div class="form-group">
<label>Имэйл:</label>
<input type="email" name="email">
</div>

<button type="submit" class="btn btn-primary">Илгээх</button>
</form>
</div>
```

### Жагсаалт:
```html
<div class="content-list">
<h3>Жагсаалт</h3>
<ul>
<li>Зүйл 1</li>
<li>Зүйл 2</li>
<li>Зүйл 3</li>
</ul>
</div>
```

### Мэдээллийн хайрцаг:
```html
<div class="info-boxes">
<div class="info-box">
<h3>Гарчиг</h3>
<p>Мэдээлэл...</p>
</div>
<div class="info-box">
<h3>Гарчиг 2</h3>
<p>Мэдээлэл 2...</p>
</div>
</div>
```

## 3-р алхам: Хөл хэсэг нэмэх

Файлын төгсгөлд:

```html
</main>

<!-- Хөл хэсэг -->
<footer class="footer">
<div class="footer-content">
<div class="footer-section">
<h3>Онлайн сургалтын систем</h3>
<p>Манай системд 1,500 гаруй оюутан, 200 гаруй багш нар идэвхтэй ажиллаж байна.</p>
<p><strong>Хаяг:</strong> Улаанбаатар хот, Сүхбаатар дүүрэг, 1-р хороо</p>
</div>
<div class="footer-section">
<h3>Холбоос</h3>
<ul>
<li><a href="../member6/contact.html">Холбоо барих</a></li>
<li><a href="../member6/policies.html">Дүрэм журам</a></li>
<li><a href="../member6/privacy.html">Нууцлалын бодлого</a></li>
<li><a href="../member6/terms.html">Үйлчилгээний нөхцөл</a></li>
<li><a href="../member6/admin.html">Администрацийн хэсэг</a></li>
</ul>
</div>
<div class="footer-section">
<h3>Холбогдох</h3>
<p><strong>Утас:</strong> 77001122, 99112233</p>
<p><strong>Факс:</strong> 70111222</p>
<p><strong>Імэйл:</strong> info@edu.mn</p>
<p><strong>Ажлын цаг:</strong> Даваа-Баасан 09:00-18:00</p>
</div>
</div>
<div class="footer-bottom">
© 2025 Онлайн сургалтын систем. Бүх эрх хуулиар хамгаалагдсан. | Хөгжүүлсэн: Веб хөгжүүлэлтийн баг
</div>
</footer>

</div>
</body>
</html>
```

## Чухал санамж:

1. **member** folder-т байгаа файлууд бол холбоосонд `../` нэм (жишээ: `../index.html`, `../images/logo.png`)
2. **Үндсэн** файлууд (index, login, register) бол `../` хэрэггүй
3. Хуучин `<table>`, `<font>` тагуудыг устгаад, шинэ `<div class="...">` ашигла
4. Өнгө, хэмжээ нь автоматаар CSS-ээс ирнэ

## Ажлын хуваарилалт:

- Гишүүн 1: member1/*.html (5 файл)
- Гишүүн 2: member2/*.html (5 файл)  
- Гишүүн 3: member3/*.html (5 файл)
- Гишүүн 4: member4/*.html (5 файл)
- Гишүүн 5: member5/*.html (5 файл)
- Гишүүн 6: member6/*.html (8 файл)

Хамтдаа: login.html, register.html шинэчлэх

## Шалгалт:

HTML файлаа browser дээр нээж, дараах зүйлсийг шалга:
- Толгой хэсэг харагдаж байна уу?
- Навигацийн цэс харагдаж байна уу?
- Агуулга зөв харагдаж байна уу?
- Хөл хэсэг харагдаж байна уу?
- Өнгө, загвар нэгдсэн байна уу?
