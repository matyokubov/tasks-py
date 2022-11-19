# Input
a = int(input("km -> "))

m = a*1000
dm = a*10000
sm = a*100000
mm = a*1000000

# Output
res = '''
{km} km = {metr} metr
{km} km = {detsimetr} detsimetr
{km} km = {santimetr} santimetr
{km} km = {millimetr} millimetr
'''.format(km=a,
        metr=m,
        detsimetr=dm,
        santimetr=sm,
        millimetr=mm)

print(res)