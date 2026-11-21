import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# ==========================================
# شبیه‌سازی مسئله فیلسوفان غذا خور بر اساس اولویت LJF (با نقص)
# شبیه‌سازی مسئله فیلسوفان غذا خور با اولویت‌بندی LJF (شامل نقص)
# ==========================================

class Philosopher:
    def __init__(self, id, think_time, eat_time):
        self.id = id
        self.think_time = think_time
        self.eat_time = eat_time  # در LJF، این به عنوان "طول کار" در نظر گرفته می‌شود / در LJF به عنوان "طول کار" در نظر گرفته می‌شود
        self.state = 'THINKING'
        self.wait_start = 0
        self.hungry_time = 0  # ثبت زمان انتظار / ثبت زمان انتظار

def run_ljf_simulation(num_philosophers=5, simulation_time=100):
    # تنظیم مدت زمان فکر کردن و غذا خوردن به صورت تصادفی
    # به صورت تصادفی مدت زمان فکر کردن و غذا خوردن را تنظیم کنید
    np.random.seed(42)
    philosophers = []
    for i in range(num_philosophers):
        # مدت زمان غذا خوردن به عنوان "طول کار" در LJF استفاده می‌شود
        # مدت زمان غذا خوردن به عنوان "طول کار" برای مرتب‌سازی LJF استفاده می‌شود
        think_t = np.random.randint(2, 5)
        eat_t = np.random.randint(5, 15) 
        philosophers.append(Philosopher(i, think_t, eat_t))
    
    # شبیه‌سازی تخصیص چاپستیک (منطق ساده شده: بررسی تصاحب چاپستیک چپ و راست)
    # شبیه‌سازی تخصیص چاپستیک (منطق ساده شده: بررسی تصاحب چاپستیک چپ و راست)
    # 0: آزاد، 1: اشغال شده
    chopsticks = [0] * num_philosophers
    
    # ثبت رویدادها برای رسم نمودار گانت
    # رویدادها را برای رسم نمودار گانت ثبت کنید
    # فرمت: (philosopher_id, start_time, end_time, action)
    events = []
    
    current_time = 0
    # صف انتظار: فیلسوفانی که گرسنه هستند
    # صف انتظار: فیلسوفانی که گرسنه هستند
    hungry_queue = []
    
    # مقداردهی اولیه: همه شروع به فکر کردن می‌کنند
    # مقداردهی اولیه: همه شروع به فکر کردن می‌کنند
    for p in philosophers:
        p.state = 'THINKING'
        events.append((p.id, 0, p.think_time, 'Thinking'))
        current_time = max(current_time, p.think_time) # زمان پایان فکر کردن
    
    # شبیه‌سازی ساده حلقه رویداد
    # شبیه‌سازی ساده حلقه رویداد
    # نکته: در اینجا فقط سعی می‌کنیم نشان دهیم که چگونه فیلسوفان با زمان غذا خوردن طولانی‌تر منابع را اشغال می‌کنند
    # نکته: در اینجا فقط سعی می‌کنیم نشان دهیم که چگونه فیلسوفان با زمان غذا خوردن طولانی‌تر منابع را اشغال می‌کنند
    # منجر به انتظار فیلسوفان با زمان غذا خوردن کوتاه‌تر می‌شود
    # و باعث می‌شود فیلسوفان با زمان غذا خوردن کوتاه‌تر منتظر بمانند
    
    # به زبان ساده: مرتب‌سازی بر اساس مدت زمان غذا خوردن (LJF)
    # به زبان ساده: مرتب‌سازی بر اساس مدت زمان غذا خوردن (LJF)
    # فرض کنید همه در زمان T به طور همزمان گرسنه می‌شوند و برای منابع رقابت می‌کنند
    # فرض کنید همه در زمان T به طور همزمان گرسنه می‌شوند و برای منابع رقابت می‌کنند
    # این اغراق‌آمیز است، اما مشکل اولویت‌بندی LJF را نشان می‌دهد
    # این اغراق‌آمیز است، اما مشکل اولویت‌بندی LJF را نشان می‌دهد
    
    # مرتب‌سازی بر اساس زمان غذا خوردن به ترتیب نزولی (LJF)
    # مرتب‌سازی بر اساس زمان غذا خوردن به ترتیب نزولی (LJF)
    sorted_philosophers = sorted(philosophers, key=lambda x: x.eat_time, reverse=True)
    
    # ثبت زمان شروع غذا خوردن هر فیلسوف
    # زمان شروع غذا خوردن هر فیلسوف را ثبت کنید
    # فرض کنید آنها به ترتیب اجرا می‌شوند (LJF غیرقابل قبضه)
    # فرض کنید آنها به ترتیب اجرا می‌شوند (LJF غیرقابل قبضه)
    current_start = 10 # فرض کنید همه در زمان 10 گرسنه می‌شوند / فرض کنید همه در زمان 10 گرسنه می‌شوند
    
    for p in sorted_philosophers:
        # شبیه‌سازی زمان انتظار
        # شبیه‌سازی زمان انتظار
        wait_time = current_start - 10
        p.hungry_time = wait_time
        
        # ثبت رویداد غذا خوردن
        # ثبت رویداد غذا خوردن
        events.append((p.id, current_start, current_start + p.eat_time, 'Eating'))
        
        # به‌روزرسانی زمان
        # به‌روزرسانی زمان
        current_start += p.eat_time
        
    return philosophers, events

# اجرای شبیه‌سازی
philosophers, events = run_ljf_simulation()

# ==========================================
# رسم نمودار گانت و نمودار زمان انتظار
# رسم نمودار گانت و نمودار زمان انتظار
# ==========================================

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# 1. نمودار گانت
# 1. نمودار گانت
colors = {'Thinking': '#A0CBE8', 'Eating': '#FFBE7D', 'Waiting': '#D3D3D3'}

for event in events:
    pid, start, end, action = event
    # رسم Thinking و Eating
    # رسم Thinking و Eating
    ax1.barh(pid, end - start, left=start, height=0.5, color=colors.get(action, 'gray'), edgecolor='black')
    ax1.text((start + end) / 2, pid, action, ha='center', va='center', fontsize=8, color='black')

# علامت‌گذاری زمان انتظار (گرسنگی) در نمودار گانت
# علامت‌گذاری زمان انتظار (گرسنگی) در نمودار گانت
for p in philosophers:
    # اگر زمان انتظار وجود دارد، در نمودار گانت نمایش دهید
    # اگر زمان انتظار وجود دارد، در نمودار گانت نمایش دهید
    # از زمان 10 تا شروع غذا خوردن
    # از زمان 10 تا شروع غذا خوردن
    if p.hungry_time > 0:
        start_wait = 10
        # یافتن رویداد غذا خوردن
        # یافتن رویداد غذا خوردن
        eat_event = next((e for e in events if e[0] == p.id and e[3] == 'Eating'), None)
        if eat_event:
            eat_start = eat_event[1]
            ax1.barh(p.id, eat_start - start_wait, left=start_wait, height=0.5, color=colors['Waiting'], edgecolor='black', hatch='//')
            ax1.text((start_wait + eat_start) / 2, p.id, f'Wait: {p.hungry_time}', ha='center', va='center', fontsize=8, color='red')

ax1.set_xlabel('Time (units)')
ax1.set_ylabel('Philosopher ID')
ax1.set_title('Gantt Chart: LJF Scheduling in Dining Philosophers (Illustrating Starvation)')
ax1.set_yticks(range(len(philosophers)))
ax1.set_yticklabels([f'P{p.id}' for p in philosophers])
ax1.grid(True, axis='x', linestyle='--', alpha=0.7)

# 2. نمودار میله‌ای زمان انتظار
# 2. نمودار میله‌ای زمان انتظار
p_ids = [f'P{p.id}' for p in philosophers]
wait_times = [p.hungry_time for p in philosophers]
eat_times = [p.eat_time for p in philosophers]

x = np.arange(len(p_ids))
width = 0.35

bars1 = ax2.bar(x - width/2, wait_times, width, label='Waiting Time', color='#E15759')
bars2 = ax2.bar(x + width/2, eat_times, width, label='Eating Time (Priority in LJF)', color='#4E79A7')

ax2.set_xlabel('Philosopher')
ax2.set_ylabel('Time (units)')
ax2.set_title('Waiting Time vs Eating Time (LJF prioritizes longer eating times)')
ax2.set_xticks(x)
ax2.set_xticklabels(p_ids)
ax2.legend()
ax2.grid(True, axis='y', linestyle='--', alpha=0.7)

# افزودن برچسب‌های داده
# افزودن برچسب‌های داده
for bar in bars1:
    height = bar.get_height()
    ax2.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom')

plt.tight_layout()
plt.savefig('ljf_dining_philosophers.png', dpi=150)
plt.show()

# ==========================================
# تولید خروجی متنی
# ==========================================
print("="*60)
print("LJF Scheduling Simulation Results")
print("="*60)
print(f"{'Philosopher':<15} {'Eat Time':<15} {'Wait Time':<15}")
print("-"*60)
for p in philosophers:
    print(f"P{p.id:<14} {p.eat_time:<15} {p.hungry_time:<15}")
print("="*60)
print("Observation: Philosophers with shorter eating times experienced")
print("significantly longer waiting times (starvation) under LJF logic.")
print("Deadlock is also possible if all grab left chopstick simultaneously.")
print("="*60)

# ذخیره در فایل
# ذخیره در فایل
with open('output.txt', 'w') as f:
    f.write("LJF Scheduling Simulation Results\n")
    f.write("="*60 + "\n")
    f.write(f"{'Philosopher':<15} {'Eat Time':<15} {'Wait Time':<15}\n")
    f.write("-"*60 + "\n")
    for p in philosophers:
        f.write(f"P{p.id:<14} {p.eat_time:<15} {p.hungry_time:<15}\n")
    f.write("="*60 + "\n")
    f.write("Conclusion: LJF is NOT suitable for Dining Philosophers.\n")
    f.write("1. It cannot prevent deadlock (circular wait can still occur).\n")
    f.write("2. It actively causes starvation for philosophers with short eating times.\n")