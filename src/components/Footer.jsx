import React from 'react';
import { Github, Linkedin, Mail, ArrowUp, Code2, Heart } from 'lucide-react';
import { personalInfo } from '../data/portfolioData';

export default function Footer() {
  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <footer className="relative border-t border-slate-200/80 dark:border-white/10 bg-white/60 dark:bg-[#040711]/90 backdrop-blur-xl py-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex flex-col md:flex-row items-center justify-between gap-6 pb-8 border-b border-slate-200/70 dark:border-white/10">
          <div className="flex items-center gap-3.5 text-center md:text-left">
            <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-blue-600 to-purple-600 flex items-center justify-center text-white font-display font-bold text-lg shadow-md">
              {personalInfo.initials}
            </div>
            <div>
              <div className="font-display font-bold text-lg text-slate-900 dark:text-white">
                {personalInfo.name}
              </div>
              <div className="text-xs font-mono text-slate-500 dark:text-slate-400">
                {personalInfo.tagline}
              </div>
            </div>
          </div>

          <div className="flex items-center gap-3">
            <a
              href={personalInfo.socials.github}
              target="_blank"
              rel="noopener noreferrer"
              aria-label="GitHub"
              className="p-3 rounded-xl glass-pill text-slate-700 dark:text-slate-300 hover:text-white hover:bg-blue-600 transition-all"
            >
              <Github className="w-4 h-4" />
            </a>
            <a
              href={personalInfo.socials.linkedin}
              target="_blank"
              rel="noopener noreferrer"
              aria-label="LinkedIn"
              className="p-3 rounded-xl glass-pill text-slate-700 dark:text-slate-300 hover:text-white hover:bg-blue-600 transition-all"
            >
              <Linkedin className="w-4 h-4" />
            </a>
            <a
              href={personalInfo.socials.email}
              aria-label="Email"
              className="p-3 rounded-xl glass-pill text-slate-700 dark:text-slate-300 hover:text-white hover:bg-purple-600 transition-all"
            >
              <Mail className="w-4 h-4" />
            </a>

            <button
              onClick={scrollToTop}
              aria-label="Back to top"
              className="ml-2 p-3 rounded-xl bg-gradient-to-r from-blue-600 to-purple-600 text-white shadow-lg shadow-blue-500/25 hover:-translate-y-1 transition-transform"
              title="Back to top"
            >
              <ArrowUp className="w-4 h-4" />
            </button>
          </div>
        </div>

        <div className="pt-6 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-slate-500 dark:text-slate-400">
          <p>
            © {new Date().getFullYear()} <strong>{personalInfo.name}</strong>. All rights reserved.
          </p>
          <p className="flex items-center gap-1.5 font-mono">
            <Code2 className="w-4 h-4 text-blue-500" />
            <span>Built with React, Vite, Tailwind CSS, Framer Motion &amp; GSAP</span>
            <Heart className="w-3.5 h-3.5 text-rose-500 fill-rose-500" />
          </p>
        </div>
      </div>
    </footer>
  );
}
