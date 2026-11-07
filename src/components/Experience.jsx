import React from 'react';
import { motion } from 'framer-motion';
import { Briefcase, Terminal, CheckCircle2, MapPin } from 'lucide-react';
import { experienceData } from '../data/portfolioData';
import SectionHeading from './SectionHeading';
import TiltCard from './TiltCard';

export default function Experience() {
  return (
    <section id="experience" className="py-20 sm:py-28 relative">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <SectionHeading
          badge="06. PRACTICAL EXPERIENCE"
          title="Development Experience &"
          highlight="Technical Training"
          subtitle="Hands-on software engineering experience across full-stack web builds, academic engineering laboratories, and industry-readiness training."
        />

        <div className="space-y-7">
          {experienceData.map((exp, index) => (
            <motion.div
              key={exp.id}
              initial={{ opacity: 0, y: 24 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, amount: 0.2 }}
              transition={{ duration: 0.5, delay: index * 0.1 }}
            >
              <TiltCard className="glass-card rounded-3xl p-6 sm:p-9 border-l-4 border-l-blue-500">
                <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-4 pb-5 mb-5 border-b border-slate-200/80 dark:border-white/10">
                  <div className="flex items-start gap-4">
                    <div className="p-3.5 rounded-2xl bg-gradient-to-br from-blue-600 to-purple-600 text-white shadow-md shrink-0">
                      <Briefcase className="w-6 h-6" />
                    </div>
                    <div>
                      <span className="inline-block px-3 py-1 rounded-full bg-blue-500/10 border border-blue-500/20 text-blue-600 dark:text-blue-400 text-xs font-mono font-semibold mb-1.5">
                        {exp.type}
                      </span>
                      <h3 className="font-display text-xl sm:text-2xl font-bold text-slate-900 dark:text-white">
                        {exp.role}
                      </h3>
                      <p className="text-sm font-medium text-slate-600 dark:text-slate-300 mt-0.5">
                        {exp.organization}
                      </p>
                    </div>
                  </div>

                  <div className="flex items-center gap-1.5 text-xs font-mono text-slate-500 dark:text-slate-400">
                    <MapPin className="w-4 h-4 text-purple-400" />
                    <span>{exp.location}</span>
                  </div>
                </div>

                <ul className="space-y-3 mb-6">
                  {exp.highlights.map((item, i) => (
                    <li
                      key={i}
                      className="flex items-start gap-3 text-sm sm:text-base text-slate-600 dark:text-slate-300"
                    >
                      <CheckCircle2 className="w-4 h-4 text-blue-500 shrink-0 mt-1" />
                      <span>{item}</span>
                    </li>
                  ))}
                </ul>

                <div className="flex flex-wrap items-center gap-2 pt-2">
                  <span className="text-xs font-mono text-slate-400 flex items-center gap-1 mr-1">
                    <Terminal className="w-3.5 h-3.5 text-blue-400" /> Stack & Focus:
                  </span>
                  {exp.technologies.map((tech) => (
                    <span
                      key={tech}
                      className="px-3 py-1 rounded-lg glass-pill text-xs font-mono font-medium text-blue-600 dark:text-blue-300"
                    >
                      {tech}
                    </span>
                  ))}
                </div>
              </TiltCard>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
