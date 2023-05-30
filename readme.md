# CSSFUCK `[]+(){}`

## Version: 0.1


CSSFuck is an esoteric language that compiles to css.

By [@HaibaoM55](https://github.com/HaibaoM55)


# List of the characters:
```
a = [0]+(1)
b = [0]+(2)
c = [0]+(3)
d = [0]+(4)
e = [0]+(5)
f = [0]+(6)
g = [0]+(7)
h = [0]+(8)
i = [0]+(9)
j = [0]+(10)
k = [1]+(1)
l = [1]+(2)
m = [1]+(3)
n = [1]+(4)
o = [1]+(5)
p = [1]+(6)
q = [1]+(7)
r = [1]+(8)
s = [1]+(9)
t = [1]+(10)
u = [2]+(1)
v = [2]+(2)
w = [2]+(3)
x = [2]+(4)
y = [2]+(5)
z = [2]+(6)
```
### Example:
```
#[1]+(10)[0]+(5)[1]+(9)[1]+(10){
    [1]+(6)[1]+(5)[1]+(9)[0]+(9)[1]+(10)[0]+(9)[1]+(5)[1]+(4): [0]+(1)[0]+(2)[1]+(9)[1]+(5)[1]+(2)[2]+(1)[1]+(10)[0]+(5);
}
```
### Will compile to:
```
#test{
    position: absolute;
}
```
# Setup
```
pip install req.txt
```

### Test run:
```
python runner.py -c 1 test.css test.cssf
```
### Make the runner.py into a binary:
```
pyinstaller --onefile runner.py
```