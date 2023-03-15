# In ra các số chia hết cho 3 trong đoạn [1, 1000]
m_list = []
for n in range(1,100):
    if n % 3 == 0:
        m_list.append(n)
print(m_list)