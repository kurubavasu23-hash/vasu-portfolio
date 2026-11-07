import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import {
  Download,
  ArrowRight,
  Github,
  Linkedin,
  Mail,
  MapPin,
  Sparkles,
  GraduationCap,
  Terminal,
  Database,
  Code2,
} from 'lucide-react';
import { personalInfo } from '../data/portfolioData';
import { handleResumeDownload } from '../utils/generateResume';
import TiltCard from './TiltCard';

export default function Hero() {
  const [roleIndex, setRoleIndex] = useState(0);
  const [displayText, setDisplayText] = useState('');
  const [isDeleting, setIsDeleting] = useState(false);
  const [imgSrc, setImgSrc] = useState(personalInfo.profilePhoto);

  useEffect(() => {
    const currentRole = personalInfo.roles[roleIndex];
    const typingSpeed = isDeleting ? 45 : 90;

    const timer = setTimeout(() => {
      if (!isDeleting && displayText === currentRole) {
        setTimeout(() => setIsDeleting(true), 1600);
      } else if (isDeleting && displayText === '') {
        setIsDeleting(false);
        setRoleIndex((prev) => (prev + 1) % personalInfo.roles.length);
      } else {
        setDisplayText(
          currentRole.substring(
            0,
            displayText.length + (isDeleting ? -1 : 1)
          )
        );
      }
    }, typingSpeed);

    return () => clearTimeout(timer);
  }, [displayText, isDeleting, roleIndex]);

  const scrollToProjects = (e) => {
    e.preventDefault();
    const el = document.getElementById('projects');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  };

  return (
    <section
      id="home"
      className="relative min-h-screen flex items-center pt-28 pb-20 overflow-hidden bg-grid-pattern"
    >
      <div className="pointer-events-none absolute -top-24 -left-24 w-96 h-96 rounded-full bg-blue-600/20 dark:bg-blue-600/25 blur-[130px] animate-pulse-slow" />
      <div className="pointer-events-none absolute top-1/3 -right-24 w-[28rem] h-[28rem] rounded-full bg-purple-600/20 dark:bg-purple-600/25 blur-[140px] animate-pulse-slow" />
      <div className="pointer-events-none absolute bottom-0 left-1/3 w-80 h-80 rounded-full bg-cyan-500/15 blur-[120px]" />

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 w-full">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-8 items-center">
          <div className="lg:col-span-7 text-center lg:text-left">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.5 }}
              className="inline-flex items-center gap-2.5 px-4 py-2 rounded-full glass-pill mb-6"
            >
              <span className="relative flex h-2.5 w-2.5">
                <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75" />
                <span className="relative inline-flex rounded-full h-2.5 w-2.5 bg-emerald-500" />
              </span>
              <span className="text-xs sm:text-sm font-medium text-slate-700 dark:text-slate-200">
                Open to Software Developer & Full Stack Opportunities
              </span>
            </motion.div>

            <motion.h1
              initial={{ opacity: 0, y: 24 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.55, delay: 0.1 }}
              className="font-display text-4xl sm:text-5xl xl:text-6xl font-extrabold tracking-tight text-slate-900 dark:text-white leading-[1.12] mb-4"
            >
              Hi, I&apos;m{' '}
              <span className="text-gradient">Kuruba Vasu</span>
            </motion.h1>

            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.55, delay: 0.2 }}
              className="h-10 sm:h-12 flex items-center justify-center lg:justify-start mb-5"
            >
              <span className="font-mono text-lg sm:text-2xl lg:text-3xl font-semibold text-blue-600 dark:text-blue-400">
                &gt; {displayText}
                <span className="inline-block w-2.5 h-6 sm:h-7 ml-1 bg-purple-500 animate-pulse align-middle" />
              </span>
            </motion.div>

            <motion.p
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.55, delay: 0.3 }}
              className="text-slate-600 dark:text-slate-300 text-base sm:text-lg leading-relaxed max-w-2xl mx-auto lg:mx-0 mb-6"
            >
              B.Tech Computer Science &amp; Engineering student at{' '}
              <span className="font-semibold text-slate-900 dark:text-white">
                {personalInfo.college}
              </span>{' '}
              (CGPA: <span className="text-blue-500 font-bold">{personalInfo.cgpa}</span>). Passionate about building scalable web applications with{' '}
              <span className="text-slate-900 dark:text-white font-medium">
                Python, Django, REST APIs, React.js, and MySQL
              </span>
              .
            </motion.p>

            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.55, delay: 0.35 }}
              className="flex flex-wrap items-center justify-center lg:justify-start gap-3 mb-8 text-xs sm:text-sm text-slate-600 dark:text-slate-400"
            >
              <span className="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-xl glass-pill">
                <MapPin className="w-4 h-4 text-blue-500" />
                {personalInfo.location}
              </span>
              <span className="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-xl glass-pill">
                <GraduationCap className="w-4 h-4 text-purple-500" />
                B.Tech CSE • CGPA {personalInfo.cgpa}
              </span>
            </motion.div>

            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.55, delay: 0.42 }}
              className="flex flex-col sm:flex-row items-center justify-center lg:justify-start gap-4 mb-9"
            >
              <button
                onClick={handleResumeDownload}
                className="w-full sm:w-auto btn-primary group"
              >
                <Download className="w-5 h-5 group-hover:-translate-y-0.5 transition-transform" />
                <span>Download Resume</span>
              </button>

              <a
                href="#projects"
                onClick={scrollToProjects}
                className="w-full sm:w-auto btn-secondary group"
              >
                <span>Explore My Work</span>
                <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform text-blue-500" />
              </a>
            </motion.div>

            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.55, delay: 0.5 }}
              className="flex items-center justify-center lg:justify-start gap-4"
            >
              <span className="text-xs font-mono uppercase tracking-wider text-slate-500 dark:text-slate-400">
                Connect:
              </span>
              <a
                href={personalInfo.socials.github}
                target="_blank"
                rel="noopener noreferrer"
                aria-label="GitHub Profile"
                className="p-3 rounded-xl glass-pill text-slate-700 dark:text-slate-200 hover:text-white hover:bg-blue-600 dark:hover:bg-blue-600 hover:border-blue-500 transition-all hover:-translate-y-1"
              >
                <Github className="w-5 h-5" />
              </a>
              <a
                href={personalInfo.socials.linkedin}
                target="_blank"
                rel="noopener noreferrer"
                aria-label="LinkedIn Profile"
                className="p-3 rounded-xl glass-pill text-slate-700 dark:text-slate-200 hover:text-white hover:bg-blue-600 dark:hover:bg-blue-600 hover:border-blue-500 transition-all hover:-translate-y-1"
              >
                <Linkedin className="w-5 h-5" />
              </a>
              <a
                href={personalInfo.socials.email}
                aria-label="Send Email"
                className="p-3 rounded-xl glass-pill text-slate-700 dark:text-slate-200 hover:text-white hover:bg-purple-600 dark:hover:bg-purple-600 hover:border-purple-500 transition-all hover:-translate-y-1"
              >
                <Mail className="w-5 h-5" />
              </a>
            </motion.div>
          </div>

          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.65, delay: 0.25 }}
            className="lg:col-span-5 flex justify-center"
          >
            <div className="relative w-full max-w-sm sm:max-w-md">
              <div className="absolute -inset-2 rounded-[2.2rem] bg-gradient-to-r from-blue-500 via-purple-500 to-cyan-400 opacity-35 blur-xl animate-pulse-slow" />

              <TiltCard className="glass-card rounded-[2rem] p-6 sm:p-7 relative">
                <div className="flex items-center justify-between pb-4 mb-5 border-b border-slate-200/70 dark:border-white/10">
                  <div className="flex items-center gap-2">
                    <span className="w-3 h-3 rounded-full bg-rose-500" />
                    <span className="w-3 h-3 rounded-full bg-amber-400" />
                    <span className="w-3 h-3 rounded-full bg-emerald-500" />
                  </div>
                  <span className="font-mono text-xs text-slate-500 dark:text-slate-400">
                    kuruba_vasu.py
                  </span>
                  <Sparkles className="w-4 h-4 text-blue-400" />
                </div>

                <div className="relative mx-auto w-56 h-56 sm:w-64 sm:h-64 rounded-2xl overflow-hidden border-2 border-blue-500/30 shadow-2xl mb-6 bg-[#0a0f24] group">
                  <img
                    src={imgSrc}
                    onError={() => setImgSrc(personalInfo.fallbackPhoto)}
                    alt={personalInfo.name}
                    className="w-full h-full object-cover object-center group-hover:scale-105 transition-transform duration-500"
                  />
                  <div className="absolute inset-0 bg-gradient-to-t from-[#050816]/80 via-transparent to-transparent" />
                  <div className="absolute bottom-3 left-3 right-3 flex items-center justify-between px-3 py-1.5 rounded-xl bg-black/60 backdrop-blur-md border border-white/15 text-xs text-white">
                    <span className="font-semibold">{personalInfo.name}</span>
                    <span className="font-mono text-cyan-400">CGPA {personalInfo.cgpa}</span>
                  </div>
                </div>

                <div className="grid grid-cols-3 gap-2.5 text-center">
                  <div className="p-2.5 rounded-xl glass-pill flex flex-col items-center gap-1">
                    <Terminal className="w-4 h-4 text-blue-500" />
                    <span className="text-xs font-semibold text-slate-800 dark:text-slate-200">
                      Python
                    </span>
                    <span className="text-[10px] font-mono text-slate-500 dark:text-slate-400">
                      Django / API
                    </span>
                  </div>
                  <div className="p-2.5 rounded-xl glass-pill flex flex-col items-center gap-1">
                    <Code2 className="w-4 h-4 text-cyan-400" />
                    <span className="text-xs font-semibold text-slate-800 dark:text-slate-200">
                      React.js
                    </span>
                    <span className="text-[10px] font-mono text-slate-500 dark:text-slate-400">
                      Frontend UI
                    </span>
                  </div>
                  <div className="p-2.5 rounded-xl glass-pill flex flex-col items-center gap-1">
                    <Database className="w-4 h-4 text-purple-400" />
                    <span className="text-xs font-semibold text-slate-800 dark:text-slate-200">
                      MySQL
                    </span>
                    <span className="text-[10px] font-mono text-slate-500 dark:text-slate-400">
                      Relational DB
                    </span>
                  </div>
                </div>
              </TiltCard>
            </div>
          </motion.div>
        </div>
      </div>
    </section>
  );
}
