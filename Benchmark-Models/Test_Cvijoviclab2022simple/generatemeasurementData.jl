# s' = 5s,    s(0) = 8.0
# d' = 3d,    d(0) = 4.0

# s(t) = 8.0 * exp(5*t)
# d(t) = 4.0 * exp(3*t)
# s(0) = c2 = 8 
# d(0) = c1 = 4

using Distributions, Random

s(t) = 8.0 * exp(5*t)
d(t) = 4.0 * exp(3*t)

sigma_sebastian = 1.7
sigma_damiano = 1.6

d1 = Normal(0.0, sigma_sebastian)
d2 = Normal(0.0, sigma_damiano)
td1 = truncated(d1, 0.0, Inf)
td2 = truncated(d2, 0.0, Inf)

Random.seed!(123);

for t = 0:0.1:1.0
    println(s(t)+rand(td1))#,"\t",t)
end
for t = 0:0.1:1.0
    println(d(t)+rand(td2))#,"\t",t)
end
