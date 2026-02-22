<template>
  <main class="home">
    <section class="hero">
      <h1>Your news, your way.</h1>
      <p>
        Paper Boy sends you AI-generated newsletters on any topic you choose,
        on a schedule that works for you.
      </p>
      <div class="cta">
        <RouterLink to="/register" class="btn btn-primary">Get started — it's free</RouterLink>
        <RouterLink to="/login" class="btn btn-ghost">Sign in</RouterLink>
      </div>
    </section>

    <section class="features">
      <div class="feature">
        <h3>Pick your topics</h3>
        <p>Describe anything — a niche technology, a sports team, a scientific field, a market.</p>
      </div>
      <div class="feature">
        <h3>Choose your cadence</h3>
        <p>Daily, weekly, bi-weekly, or monthly. Paper Boy adapts to your reading habits.</p>
      </div>
      <div class="feature">
        <h3>Delivered to your inbox</h3>
        <p>AI scans recent sources and writes a clean summary — straight to your email.</p>
      </div>
    </section>
  </main>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
.home {
  max-width: 900px;
  margin: 0 auto;
  padding: 4rem 1.5rem;
}

.hero {
  text-align: center;
  margin-bottom: 5rem;
}

.hero h1 {
  font-size: 3rem;
  font-weight: 700;
  line-height: 1.1;
  margin-bottom: 1rem;
}

.hero p {
  font-size: 1.2rem;
  color: #555;
  max-width: 560px;
  margin: 0 auto 2rem;
}

.cta {
  display: flex;
  gap: 1rem;
  justify-content: center;
}

.btn {
  padding: 0.75rem 1.75rem;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  border: none;
  transition: opacity 0.15s;
}

.btn:hover { opacity: 0.85; }

.btn-primary {
  background: #1a1a1a;
  color: #fff;
}

.btn-ghost {
  background: transparent;
  color: #1a1a1a;
  border: 2px solid #1a1a1a;
}

.features {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 2rem;
}

.feature {
  background: #fff;
  border-radius: 12px;
  padding: 1.75rem;
  box-shadow: 0 1px 4px rgba(0,0,0,.06);
}

.feature h3 {
  margin-bottom: 0.5rem;
  font-size: 1.1rem;
}

.feature p {
  color: #555;
  font-size: 0.95rem;
}
</style>
