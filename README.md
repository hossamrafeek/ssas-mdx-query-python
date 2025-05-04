# Query SSAS Tabular Data Using Python and ADOMD.NET

This project provides a working example of querying **SQL Server Analysis Services (SSAS)** tabular models using **Python** and **ADOMD.NET**.  
It demonstrates how to execute **MDX queries** and read results programmatically.

> ✅ Useful for data engineers, BI developers, data scientists, and anyone working with SSAS cubes.

---

## 🚀 Features

- Connect to SSAS Tabular using Python
- Execute MDX queries
- Read and print results
- Supports Integrated Security (Windows Authentication)

---

## 📚 Prerequisites

1. **Python for .NET (Pythonnet)**
   - Install using pip:
     ```bash
     pip install pythonnet
     ```

2. **ADOMD.NET Client Library**
   - Download and install:
     - [Microsoft ADOMD.NET](https://www.microsoft.com/en-us/download/details.aspx?id=58255)

3. **Access to an SSAS Tabular instance**
   - Ensure you have:
     - SSAS Server Name
     - Database Name
     - Cube Name
     - Necessary user permissions

---

## 📝 How to Use

1. Clone the repo:
   ```bash
   git clone https://github.com/YourUsername/ssas-mdx-query-python.git
   cd ssas-mdx-query-python
````

2. Update connection settings in `query_ssas_example.py`:

   ```python
   SERVER_NAME = "YOUR_SSAS_SERVER"
   DATABASE_NAME = "YOUR_DATABASE_NAME"
   ```

3. Update MDX query (replace `YOUR_CUBE_NAME`):

   ```mdx
   FROM [YOUR_CUBE_NAME]
   ```

4. Run the script:

   ```bash
   python query_ssas_example.py
   ```

---

## ✅ Example Output

```
Year    S_Value
2020    123456.78
2021    234567.89
2022    345678.90
```

---

## 📦 Project Structure

```
ssas-mdx-query-python/
│
├── query_ssas_example.py   # Main Python script
├── README.md               # This documentation
└── LICENSE                 # MIT License
```

---

## 💡 Notes

* This example uses **Windows Authentication** (`Integrated Security=SSPI`).
* Ensure your machine has access to the SSAS instance.
* For complex queries, modify the MDX statement in the script.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) — free for personal and commercial use.

---

## 🤝 Contributing

Feel free to fork this repo, suggest improvements, or submit pull requests to make this resource better for the community!

---

## 🙏 Acknowledgments

Special thanks to the data engineering and BI community for continuous sharing and knowledge exchange.

---

```

---

