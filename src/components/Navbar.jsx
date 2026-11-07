import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import {
  Menu,
  X,
  Sun,
  Moon,
  Download,
  Code2,
  ChevronRight,
} from 'lucide-react';
import { personalInfo } from '../data/portfolioData';
import { handleResumeDownload } from '../utils/generateResume';

const navLinks = [
  { name: 'Home', href: '#home' },
  { name: 'About', href: '#about' },
  { name: 'Skills', href: '#skills' },
  { name: 'Projects', href: '#projects' },
  { name: 'Education', href: '#education' },
  { name: 'Certifications', href: '#certifications' },
  { name: 'Experience', href: '#experience' },
  { name: 'Contact', href: '#contact' },
];

export default function Navbar({ isDark, toggleTheme }) {
  const [scrolled, setScrolled] = useState(false);
  const [activeSection, setActiveSection] = useState('home');
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 24);

      const sections = navLinks.map((link) => link.href.substring(1));
      const scrollPosition = window.scrollY + 180;

      for (const sectionId of sections) {
        const el = document.getElementById(sectionId);
        if (el) {
          const top = el.offsetTop;
          const height = el.offsetHeight;
          if (scrollPosition >= top && scrollPosition < top + height) {
            setActiveSection(sectionId);
            break;
          }
        }
      }
    };

    window.addEventListener('scroll', handleScroll, { passive: true });
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const handleNavClick = (e, href) => {
    e.preventDefault();
    setMobileMenuOpen(false);
    const target = document.querySelector(href);
    if (target) {
      target.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <header
      className={`fixed top-0 left-0 right-0 z-40 transition-all duration-300 ${
        scrolled
          ? 'py-3 bg-white/85 dark:bg-[#050816]/85 backdrop-blur-xl border-b border-slate-200/80 dark:border-white/10 shadow-lg shadow-black/5'
          : 'py-5 bg-transparent'
      }`}
    >
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between">
        <a
          href="#home"
          onClick={(e) => handleNavClick(e, '#home')}
          className="flex items-center gap-3 group focus:outline-none"
        >
          <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-blue-600 via-indigo-600 to-purple-600 flex items-center justify-center text-white font-display font-bold text-lg shadow-md shadow-blue-500/25 group-hover:scale-105 transition-transform">
            {personalInfo.initials}
          </div>
          <div className="flex flex-col">
            <span className="font-display font-bold text-base sm:text-lg tracking-tight text-slate-900 dark:text-white leading-none">
              {personalInfo.name}
            </span>
            <span className="font-mono text-[11px] text-blue-600 dark:text-blue-400 mt-0.5 flex items-center gap-1">
              <Code2 className="w-3 h-3" /> Full Stack Dev
            </span>
          </div>
        </a>

        <nav className="hidden xl:flex items-center gap-1 p-1.5 rounded-2xl glass-pill">
          {navLinks.map((link) => {
            const isActive = activeSection === link.href.substring(1);
            return (
              <a
                key={link.name}
                href={link.href}
                onClick={(e) => handleNavClick(e, link.href)}
                className={`relative px-3.5 py-2 rounded-xl text-sm font-medium transition-colors ${
                  isActive
                    ? 'text-white'
                    : 'text-slate-600 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white'
                }`}
              >
                {isActive && (
                  <motion.span
                    layoutId="activeNavIndicator"
                    className="absolute inset-0 rounded-xl bg-gradient-to-r from-blue-600 to-purple-600 -z-10 shadow-md shadow-blue-500/25"
                    transition={{ type: 'spring', stiffness: 350, damping: 30 }}
                  />
                )}
                {link.name}
              </a>
            );
          })}
        </nav>

        <div className="flex items-center gap-2.5">
          <button
            onClick={toggleTheme}
            aria-label="Toggle Dark/Light Theme"
            className="p-2.5 rounded-xl glass-pill text-slate-700 dark:text-slate-200 hover:border-blue-500/50 transition-all"
            title={isDark ? 'Switch to Light Mode' : 'Switch to Dark Mode'}
          >
            {isDark ? (
              <Sun className="w-5 h-5 text-amber-400" />
            ) : (
              <Moon className="w-5 h-5 text-indigo-600" />
            )}
          </button>

          <button
            onClick={handleResumeDownload}
            className="hidden sm:inline-flex items-center gap-2 px-4 py-2.5 rounded-xl text-xs sm:text-sm font-semibold text-white bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-500 hover:to-purple-500 shadow-md shadow-blue-500/20 transition-all"
          >
            <Download className="w-4 h-4" />
            <span>Resume</span>
          </button>

          <button
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            aria-label="Toggle Navigation Menu"
            className="xl:hidden p-2.5 rounded-xl glass-pill text-slate-800 dark:text-slate-100"
          >
            {mobileMenuOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
          </button>
        </div>
      </div>

      <AnimatePresence>
        {mobileMenuOpen && (
          <motion.div
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: 'auto' }}
            exit={{ opacity: 0, height: 0 }}
            transition={{ duration: 0.25 }}
            className="xl:hidden overflow-hidden bg-white/95 dark:bg-[#080d21]/95 backdrop-blur-2xl border-b border-slate-200 dark:border-white/10"
          >
            <div className="max-w-7xl mx-auto px-4 py-5 flex flex-col gap-2">
              {navLinks.map((link) => {
                const isActive = activeSection === link.href.substring(1);
                return (
                  <a
                    key={link.name}
                    href={link.href}
                    onClick={(e) => handleNavClick(e, link.href)}
                    className={`flex items-center justify-between px-4 py-3 rounded-xl font-medium text-sm transition-all ${
                      isActive
                        ? 'bg-gradient-to-r from-blue-600 to-purple-600 text-white shadow-md'
                        : 'text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-white/5'
                    }`}
                  >
                    <span>{link.name}</span>
                    <ChevronRight className="w-4 h-4 opacity-75" />
                  </a>
                );
              })}

              <button
                onClick={() => {
                  setMobileMenuOpen(false);
                  handleResumeDownload();
                }}
                className="mt-2 w-full btn-primary text-sm py-3"
              >
                <Download className="w-4 h-4" />
                <span>Download Resume</span>
              </button>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </header>
  );
}
