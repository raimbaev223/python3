m_earth = int(input('Enter val: '))
m_earth = m_earth - 1
for m_moon in range(m_earth, m_earth + 15):
    m_earth = m_earth + 1
    m_moon = m_earth * 0.165
    print(m_earth)
    print(m_moon)