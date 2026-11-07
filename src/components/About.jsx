import React, { useEffect, useState, useRef } from 'react';
import { motion, useInView } from 'framer-motion';
import {
  UserCheck,
  GraduationCap,
  Target,
  MapPin,
  Award,
  Code,
} from 'lucide-react';
import { personalInfo, statsData } from '../data/portfolioData';
import SectionHeading from './SectionHeading';
import TiltCard from './TiltCard';

function AnimatedCounter({ value, decimals = 0, suffix = '' }) {
  const [count, setCount] = useState(0);
  const ref = useRef(null);
  const isInView = useInView(ref, { once: true, amount: 0.4 });

  useEffect(() => {
    if (!isInView) return;

    let start = 0;
    const duration = 1600;
    const startTime = performance.now();

    const updateCounter = (currentTime) => {
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      const currentVal = start + eased * (value - start);
      setCount(currentVal);

      if (progress < 1) {
        requestAnimationFrame(updateCounter);
      } else {
        setCount(value);
      }
    };

    requestAnimationFrame(updateCounter);
  }, [isInView, value]);

  return (
    <span ref={ref}>
      {count.toFixed(decimals)}
      {suffix}
    </span>
  );
}

export default function About() {
  return (
    <section id="about" className="py-20 sm:py-28 relative">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <SectionHeading
          badge="01. ABOUT ME"
          title="Engineering Solutions with"
          highlight="Clean Code & Architecture"
          subtitle="A closer look at my academic background, technical philosophy, and software engineering career goals."
        />

        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-stretch mb-14">
          <motion.div
            initial={{ opacity: 0, x: -24 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true, amount: 0.25 }}
            transition={{ duration: 0.55 }}
            className="lg:col-span-7 glass-card rounded-3xl p-7 sm:p-9 flex flex-col justify-between"
          >
            <div>
              <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-xl bg-blue-500/10 border border-blue-500/20 text-blue-600 dark:text-blue-400 text-xs font-mono font-semibold mb-5">
                <UserCheck className="w-4 h-4" />
                <span>PROFESSIONAL INTRODUCTION</span>
              </div>

              <h3 className="font-display text-2xl sm:text-3xl font-bold text-slate-900 dark:text-white mb-4">
                Passionate Python Full Stack Developer from Kurnool, India
              </h3>

              <p className="text-slate-600 dark:text-slate-300 leading-relaxed mb-4 text-base">
                {personalInfo.bio}
              </p>

              <p className="text-slate-600 dark:text-slate-300 leading-relaxed text-base">
                Whether designing normalized relational database schemas in{' '}
                <strong className="text-slate-900 dark:text-white">MySQL</strong>, building RESTful backend workflows in{' '}
                <strong className="text-slate-900 dark:text-white">Python &amp; Django</strong>, or crafting interactive user interfaces in{' '}
                <strong className="text-slate-900 dark:text-white">React.js &amp; JavaScript</strong>, I focus on reliability, maintainability, and seamless user experience.
              </p>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-6 mt-6 border-t border-slate-200/80 dark:border-white/10">
              <div className="flex items-start gap-3">
                <div className="p-2.5 rounded-xl bg-blue-500/10 text-blue-500 mt-0.5">
                  <MapPin className="w-5 h-5" />
                </div>
                <div>
                  <div className="text-xs font-mono uppercase text-slate-400">
                    Location
                  </div>
                  <div className="text-sm font-semibold text-slate-900 dark:text-white">
                    {personalInfo.location}
                  </div>
                </div>
              </div>

              <div className="flex items-start gap-3">
                <div className="p-2.5 rounded-xl bg-purple-500/10 text-purple-500 mt-0.5">
                  <Code className="w-5 h-5" />
                </div>
                <div>
                  <div className="text-xs font-mono uppercase text-slate-400">
                    Core Focus
                  </div>
                  <div className="text-sm font-semibold text-slate-900 dark:text-white">
                    Python Full Stack &amp; Software Dev
                  </div>
                </div>
              </div>
            </div>
          </motion.div>

          <div className="lg:col-span-5 flex flex-col gap-6">
            <motion.div
              initial={{ opacity: 0, x: 24 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true, amount: 0.25 }}
              transition={{ duration: 0.55 }}
              className="glass-card rounded-3xl p-7 flex-1 relative overflow-hidden"
            >
              <div className="absolute -right-8 -top-8 w-32 h-32 rounded-full bg-blue-500/10 blur-2xl pointer-events-none" />
              <div className="flex items-center gap-3 mb-4">
                <div className="p-3 rounded-2xl bg-gradient-to-br from-blue-500 to-indigo-600 text-white shadow-md shadow-blue-500/20">
                  <GraduationCap className="w-6 h-6" />
                </div>
                <div>
                  <span className="text-xs font-mono uppercase tracking-wider text-blue-500 font-semibold">
                    Academic Profile
                  </span>
                  <h4 className="font-display text-lg font-bold text-slate-900 dark:text-white">
                    {personalInfo.education}
                  </h4>
                </div>
              </div>
              <p className="text-sm text-slate-600 dark:text-slate-300 font-medium mb-3">
                {personalInfo.college}
              </p>
              <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-xl bg-emerald-500/10 border border-emerald-500/25 text-emerald-600 dark:text-emerald-400 text-xs font-mono font-bold">
                <Award className="w-4 h-4" />
                <span>Current CGPA: {personalInfo.cgpa} / 10.0</span>
              </div>
            </motion.div>

            <motion.div
              initial={{ opacity: 0, x: 24 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true, amount: 0.25 }}
              transition={{ duration: 0.55, delay: 0.1 }}
              className="glass-card rounded-3xl p-7 flex-1 relative overflow-hidden"
            >
              <div className="absolute -right-8 -bottom-8 w-32 h-32 rounded-full bg-purple-500/10 blur-2xl pointer-events-none" />
              <div className="flex items-center gap-3 mb-4">
                <div className="p-3 rounded-2xl bg-gradient-to-br from-purple-500 to-pink-600 text-white shadow-md shadow-purple-500/20">
                  <Target className="w-6 h-6" />
                </div>
                <div>
                  <span className="text-xs font-mono uppercase tracking-wider text-purple-500 font-semibold">
                    Career Objective
                  </span>
                  <h4 className="font-display text-lg font-bold text-slate-900 dark:text-white">
                    {personalInfo.careerGoal}
                  </h4>
                </div>
              </div>
              <p className="text-sm text-slate-600 dark:text-slate-300 leading-relaxed">
                Committed to contributing high-quality full-stack code, collaborating with agile engineering teams, and continuously advancing in modern software architecture.
              </p>
            </motion.div>
          </div>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
          {statsData.map((stat, idx) => (
            <motion.div
              key={stat.id}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, amount: 0.3 }}
              transition={{ duration: 0.45, delay: idx * 0.08 }}
            >
              <TiltCard className="glass-card rounded-2xl p-6 text-center h-full border-t-2 border-t-blue-500/40">
                <div className="font-display text-3xl sm:text-4xl font-extrabold text-gradient mb-1.5">
                  <AnimatedCounter
                    value={stat.value}
                    decimals={stat.decimals}
                    suffix={stat.suffix}
                  />
                </div>
                <div className="font-semibold text-slate-900 dark:text-white text-sm sm:text-base mb-1">
                  {stat.label}
                </div>
                <p className="text-xs text-slate-500 dark:text-slate-400">
                  {stat.description}
                </p>
              </TiltCard>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
