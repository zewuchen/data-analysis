import matplotlib.pyplot as plt

x=[1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2013]
y=[116,316,352,1201,1319,1323,1036,2201,2784,2739,2921,2426,3243,3864,4097,5008,5974]
plt.plot(x,y)
plt.xlabel("Anos")
plt.ylabel("Nº Inscritos (MIL)")
plt.title("Evolução dos inscritos no Enem")
plt.show()