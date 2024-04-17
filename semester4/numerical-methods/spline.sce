t = [0,1,4,5];
y = [26,7,25,4];
n = length(t)-1;
for i=1:n,
    h(i) = t(i+1) - t(i);
    printf('h(%d): %f \n', i-1, h(i));
    b(i) = ((y(i+1) - y(i)) / h(i));
    printf('b(%d): %f \n', i-1, b(i));
end,

printf('\n');

for i=1:n-1,
    if i==1,
        u(i) = 2 * (h(i) + h(i+1));
        v(i) = 6 * (b(i+1) - b(i));
    else,
        u(i) = 2 * (h(i) + h(i+1)) - (h(i) ^ 2 / u(i-1));
        v(i) = 6 * (b(i+1) - b(i)) - ((h(i) * v(i-1)) / u(i-1));
    end,
    printf('u(%d): %f \n', i, u(i));
    printf('v(%d): %f \n', i, v(i));
end,

printf('\n');

for i=n+1:-1:1,
    if (i == n+1 || i == 1),
        z(i) = 0;
    else,
        z(i) = (v(i-1) - (h(i) * z(i+1))) / u(i-1);
    end,
    printf('z(%d): %f \n', i-1, z(i));
end,

printf('\n');

for i=1:n,
    B(i) = (((-1) * (h(i)) / 6) * z(i+1)) - ((h(i) / 3) * z(i)) + (1 / h(i)) * (y(i+1)-y(i))
    printf('B(%d): %f \n', i-1, B(i));
end,

printf('\n');

x = poly(0,"x"); 

for i=1:n,
    if i == n,
        printf('S(x) -> <%d;%d> \n', t(i), t(i+1));
    else,
        printf('S(x) -> <%d;%d) \n', t(i), t(i+1));
    end,
    S(i) = y(i) + (x - t(i)) * (B(i) + (x - t(i)) * ((z(i) / 2) + (1 / (6 * h(i)) * (x - t(i)) * (z(i+1) - z(i)))))
    disp(S(i))
    printf('\n');
end
