using Random

rng = MersenneTwister(401)
lambda, T = 2.5, 5.0
t = 0.0
czasy = Float64[]
while true
    t += randexp(rng) / lambda
    if t > T
        break
    end
    push!(czasy, t)
end
println("N_T = $(length(czasy))")
println("chwile nadejsc = $czasy")
