# s' = 5s+3d,    s(0) = 8.0
# d' = 3s+5d,    d(0) = 4.0

# s(t) = 1/2 * exp(2*t) * ( c1 * ( exp(6*t) - 1 ) + c2 * ( exp(6*t) + 1 ) )
# d(t) = 1/2 * exp(2*t) * ( c1 * ( exp(6*t) + 1 ) + c2 * ( exp(6*t) - 1 ) )
# s(0) = c2 = 8 
# d(0) = c1 = 4

# s(t) = exp(2*t) * ( 2 * ( exp(6*t) - 1 ) + 4 * ( exp(6*t) + 1 ) )
# d(t) = exp(2*t) * ( 2 * ( exp(6*t) + 1 ) + 4 * ( exp(6*t) - 1 ) )

using Distributions, Random

s(t) = exp(2*t) * ( 2 * ( exp(6*t) - 1 ) + 4 * ( exp(6*t) + 1 ) )
d(t) = exp(2*t) * ( 2 * ( exp(6*t) + 1 ) + 4 * ( exp(6*t) - 1 ) )

sigma_sebastian = 1.3
sigma_damiano = 1.5


d1 = Normal(0.0, sigma_sebastian)
d2 = Normal(0.0, sigma_damiano)
td1 = truncated(d1, 0.0, Inf)
td2 = truncated(d2, 0.0, Inf)

Random.seed!(123);

for t = 0:0.1:1.0
    println(s(t)+rand(td1),"\t",t)
end
for t = 0:0.1:1.0
    println(d(t)+rand(td2),"\t",t)
end
