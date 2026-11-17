using Random

rng = MersenneTwister(502)
mu, sigma, T, n = 0.25, 0.7, 2.0, 200
dt = T / n
dW = sqrt(dt) .* randn(rng, n)
X_em, X_exact, W = 1.0, 1.0, 0.0
for k in 1:n
    X_em *= 1 + mu * dt + sigma * dW[k]
    W += dW[k]
end
X_exact = exp((mu - sigma^2 / 2) * T + sigma * W)
println("EM = $X_em, dokladne = $X_exact")
