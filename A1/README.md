
### **Experiments using spreadsheets**

1. Create a data sheet of 10 employees with five columns:
   **Sl. No., Name, Date of Birth, Gender and Total salary.**

   a. Format the different column values for consistency with respect to currency and date formats.

   b. Add a column **Age** (Calculate the age using DOB and Current date).

   c. Calculate the income tax based on the salary using the following table:

| Income Range  | Income Tax                       |
| ------------- | -------------------------------- |
| 0–4 lakh      | Nil                              |
| 4–8 lakh      | 5% above ₹4,00,000               |
| 8–12 lakh     | ₹20,000 + 10% above ₹8,00,000    |
| 12–16 lakh    | ₹60,000 + 15% above ₹12,00,000   |
| 16–20 lakh    | ₹1,20,000 + 20% above ₹16,00,000 |
| 20–24 lakh    | ₹2,00,000 + 25% above ₹20,00,000 |
| Above 24 lakh | ₹3,00,000 + 30% above ₹24,00,000 |

d. Count the number of female employees paying income tax

e. Count the number of male employees exempted from paying tax

f. Add a column **Net Salary** which is calculated after deducting tax amount from Total salary

---

# ✅ **Solution**

## **Step 1 – Create Employee Data Sheet**

| Sl.No | Name           | DOB        | Gender | Total Salary |
| ----: | -------------- | ---------- | ------ | ------------ |
|     1 | Arjun Rao      | 15-03-1990 | Male   | 12,00,000    |
|     2 | Sneha Kulkarni | 08-10-1995 | Female | 5,40,000     |
|     3 | Rohan Patil    | 21-07-1989 | Male   | 18,50,000    |
|     4 | Harsha Shetty  | 11-11-1993 | Male   | 4,00,000     |
|     5 | Deepa Pai      | 05-08-1991 | Female | 25,00,000    |
|     6 | Hari Hegde     | 22-06-1997 | Male   | 7,20,000     |
|     7 | Divya Nayak    | 14-02-1990 | Female | 9,00,000     |
|     8 | Vikas Kumar    | 01-12-1994 | Male   | 22,50,000    |
|     9 | Kavya Bhat     | 12-09-1998 | Female | 3,20,000     |
|    10 | Sudeep Jain    | 29-05-1987 | Male   | 16,80,000    |

---

## **Step 2 – Format Columns**

* Select **DOB column** → Format → *Date*
* Select **Total Salary column** → Format → *Currency ₹*

---

## **Step 3 – Add Age column**

Formula for Age (DOB in column C row 2):

```excel
=DATEDIF(C2, TODAY(), "Y")
```

Copy downward.

---

## **Step 4 – Calculate Income Tax**

Assume salary in column **E2**

```excel
=IF(E2<=400000,0,
 IF(E2<=800000,(E2-400000)*0.05,
 IF(E2<=1200000,20000+(E2-800000)*0.1,
 IF(E2<=1600000,60000+(E2-1200000)*0.15,
 IF(E2<=2000000,120000+(E2-1600000)*0.2,
 IF(E2<=2400000,200000+(E2-2000000)*0.25,
 300000+(E2-2400000)*0.3
)))))) 
```

Copy downward to all rows.

---

## **Step 5 – Count Female employees paying Tax**

Assuming Tax column = F2:F11
Gender column = D2:D11

```excel
=COUNTIFS(F2:F11,">0",D2:D11,"Female")
```

---

## **Step 6 – Count Male employees exempted**

```excel
=COUNTIFS(F2:F11,"=0",D2:D11,"Male")
```

---

## **Step 7 – Add Net Salary column**

Formula:

```excel
=E2 - F2
```

Copy to all rows.

---

# ⭐ Final Result Columns

Your spreadsheet now contains:

* Sl.No
* Name
* DOB
* Gender
* Total Salary
* Age
* Income Tax
* Net Salary
