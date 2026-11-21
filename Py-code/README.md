# LJF Scheduling in the Dining Philosophers Problem

## 📌 Overview / مرور کلی

This project demonstrates why the **Longest Job First (LJF)** scheduling algorithm is **not suitable** for solving the classic **Dining Philosophers** concurrency problem. It provides an educational Python simulation with meaningful comments (English & Persian) and visualization outputs.

این پروژه نشان می‌دهد که چرا الگوریتم زمان‌بندی **Longest Job First (LJF)** برای حل مسئله کلاسیک همزمانی **فیلسوفان غذاخور** **مناسب نیست**. این پروژه شامل یک شبیه‌سازی آموزشی پایتون با کامنت‌های معنادار (انگلیسی و فارسی) و خروجی‌های تصویری است.

---

## 🎯 Key Findings / یافته‌های کلیدی

| Aspect | Result |
|--------|--------|
| **Deadlock Prevention** | ❌ LJF cannot prevent deadlock (circular wait still possible) |
| **Starvation Prevention** | ❌ LJF actively **causes** starvation for short-job philosophers |
| **Fairness** | ❌ Longest eaters always win, shortest may never eat |
| **Suitability for Dining Philosophers** | ❌ Not recommended |

| جنبه | نتیجه |
|------|-------|
| **جلوگیری از بن‌بست** | ❌ LJF نمی‌تواند از بن‌بست جلوگیری کند |
| **جلوگیری از گرسنگی** | ❌ LJF به طور فعال باعث گرسنگی فیلسوفان با زمان کوتاه می‌شود |
| **عدالت** | ❌ همیشه فیلسوفان با زمان طولانی برنده می‌شوند |
| **مناسب بودن برای مسئله** | ❌ توصیه نمی‌شود |

---

## 🧠 Why LJF Fails / چرا LJF شکست می‌خورد

1. **LJF is a CPU scheduling algorithm, not a resource allocation protocol.**
   LJF decides *which process runs first*, not *how to acquire two resources atomically*. The Dining Philosophers problem requires atomic acquisition of two chopsticks — LJF does nothing to address this.

2. **Circular wait is still possible.**
   If all philosophers grab their left chopstick simultaneously, a deadlock cycle forms regardless of LJF priority ordering.

3. **Starvation is inherent to LJF.**
   By definition, LJF prioritizes longer jobs. Philosophers with short eating times can be indefinitely postponed → **starvation**.

4. **No priority aging mechanism.**
   Standard LJF has no built-in aging, so waiting philosophers never gain priority over time.

---

## 📁 Project Structure / ساختار پروژه
├── ljf_dining_philosophers.py # Main simulation script /  اسکریپت اصلی شبیه‌سازی <br>
├── code-Preview.jpg # Code image preview <br>
├── ljf_dining_philosophers.jpg # Generated charts / نمودارهای تولید شده <br>
├── output.txt # Text results / خروجی متنی <br>
├── output.jpg # image results  <br>
└── README.md # This file / همین فایل

---

## ⚙️ Requirements / پیش‌نیازها

- Python 3.7+
- `matplotlib`
- `numpy`


