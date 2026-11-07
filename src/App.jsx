import React, { useState, useEffect } from 'react';
import { motion, useScroll, useSpring } from 'framer-motion';
import Loader from './components/Loader';
import CustomCursor from './components/CustomCursor';
import ParticleBackground from './components/ParticleBackground';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import About from './components/About';
import Skills from './components/Skills';
import Projects from './components/Projects';
import Education from './components/Education';
import Certifications from './components/Certifications';
import Experience from './components/Experience';
import Contact from './components/Contact';
import Footer from './components/Footer';

export default function App() {
  const [isLoading, setIsLoading] = useState(true);
  const [isDark, setIsDark] = useState(true);

  const { scrollYProgress } = useScroll();
  const scaleX = useSpring(scrollYProgress, {
    stiffness: 120,
    damping: 30,
    restDelta: 0.001,
  });

  useEffect(() => {
    const savedTheme = localStorage.getItem('kv_theme');
    if (savedTheme === 'light') {
      setIsDark(false);
      document.documentElement.classList.remove('dark');
    } else {
      setIsDark(true);
      document.documentElement.classList.add('dark');
    }
  }, []);

  const toggleTheme = () => {
    setIsDark((prev) => {
      const next = !prev;
      if (next) {
        document.documentElement.classList.add('dark');
        localStorage.setItem('kv_theme', 'dark');
      } else {
        document.documentElement.classList.remove('dark');
        localStorage.setItem('kv_theme', 'light');
      }
      return next;
    });
  };

  return (
    <div className="min-h-screen bg-slate-50 dark:bg-[#050816] text-slate-900 dark:text-slate-100 relative selection:bg-blue-600 selection:text-white transition-colors duration-300">
      {isLoading && <Loader onComplete={() => setIsLoading(false)} />}

      <motion.div
        className="fixed top-0 left-0 right-0 h-1 bg-gradient-to-r from-blue-500 via-purple-500 to-cyan-400 origin-left z-50"
        style={{ scaleX }}
      />

      <CustomCursor />
      <ParticleBackground isDark={isDark} />

      <Navbar isDark={isDark} toggleTheme={toggleTheme} />
      <main className="relative z-10">
        <Hero />
        <About />
        <Skills />
        <Projects />
        <Education />
        <Certifications />
        <Experience />
        <Contact />
      </main>
      <Footer />
    </div>
  );
}
