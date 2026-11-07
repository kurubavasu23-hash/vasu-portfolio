import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import {
  Terminal,
  Code2,
  Coffee,
  Layout,
  Palette,
  Atom,
  Server,
  Webhook,
  Cpu,
  Database,
  Table,
  GitBranch,
  Github,
  Code,
  BarChart3,
  Network,
  HardDrive,
  Layers,
  Globe,
} from 'lucide-react';
import { skillCategories, skillsData } from '../data/portfolioData';
import SectionHeading from './SectionHeading';
import TiltCard from './TiltCard';

const iconMap = {
  Terminal,
  Code2,
  Coffee,
  Layout,
  Palette,
  Atom,
  Server,
  Webhook,
  Cpu,
  Database,
  Table,
  GitBranch,
  Github,
  Code,
  BarChart3,
  Network,
  HardDrive,
  Layers,
  Globe,
};

export default function Skills() {
  const [selectedCategory, setSelectedCategory] = useState('All');

  const filteredSkills =
    selectedCategory === 'All'
      ? skillsData
      : skillsData.filter((s) => s.category === selectedCategory);

  return (
    <section id="skills" className="py-20 sm:py-28 relative">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <SectionHeading
          badge="02. TECHNICAL ARSENAL"
          title="Skills, Technologies &"
          highlight="CS Foundations"
          subtitle="Comprehensive proficiency across full-stack development, relational databases, developer tooling, and core computer science subjects."
        />

        <div className="flex flex-wrap items-center justify-center gap-2 sm:gap-3 mb-12">
          {skillCategories.map((category) => {
            const isActive = selectedCategory === category;
            return (
              <button
                key={category}
                onClick={() => setSelectedCategory(category)}
                className={`relative px-4 py-2.5 rounded-xl text-xs sm:text-sm font-semibold transition-all ${
                  isActive
                    ? 'text-white shadow-lg shadow-blue-500/25'
                    : 'glass-pill text-slate-600 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white'
                }`}
              >
                {isActive && (
                  <motion.span
                    layoutId="activeSkillCategory"
                    className="absolute inset-0 rounded-xl bg-gradient-to-r from-blue-600 to-purple-600 -z-10"
                    transition={{ type: 'spring', stiffness: 350, damping: 28 }}
                  />
                )}
                {category}
              </button>
            );
          })}
        </div>

        <motion.div
          layout
          className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6"
        >
          <AnimatePresence mode="popLayout">
            {filteredSkills.map((skill) => {
              const IconComponent = iconMap[skill.icon] || Code2;
              return (
                <motion.div
                  key={skill.name}
                  layout
                  initial={{ opacity: 0, scale: 0.92 }}
                  animate={{ opacity: 1, scale: 1 }}
                  exit={{ opacity: 0, scale: 0.9 }}
                  transition={{ duration: 0.3 }}
                >
                  <TiltCard className="glass-card rounded-2xl p-6 h-full flex flex-col justify-between group hover:border-blue-500/40 transition-colors">
                    <div>
                      <div className="flex items-start justify-between gap-3 mb-4">
                        <div className="flex items-center gap-3.5">
                          <div
                            className={`p-3 rounded-xl bg-gradient-to-br ${skill.color} text-white shadow-md group-hover:scale-110 transition-transform`}
                          >
                            <IconComponent className="w-5 h-5" />
                          </div>
                          <div>
                            <h3 className="font-display font-bold text-lg text-slate-900 dark:text-white">
                              {skill.name}
                            </h3>
                            <span className="text-xs font-mono text-slate-500 dark:text-slate-400">
                              {skill.category}
                            </span>
                          </div>
                        </div>

                        <span className="px-2.5 py-1 rounded-lg glass-pill text-[11px] font-mono font-semibold text-blue-600 dark:text-blue-400">
                          {skill.badge}
                        </span>
                      </div>

                      <p className="text-xs sm:text-sm text-slate-600 dark:text-slate-300 leading-relaxed mb-5">
                        {skill.description}
                      </p>
                    </div>

                    <div>
                      <div className="flex justify-between items-center text-xs font-mono mb-1.5">
                        <span className="text-slate-500 dark:text-slate-400">
                          Proficiency
                        </span>
                        <span className="font-bold text-slate-800 dark:text-slate-200">
                          {skill.level}%
                        </span>
                      </div>
                      <div className="w-full h-2 rounded-full bg-slate-200 dark:bg-white/10 overflow-hidden">
                        <motion.div
                          initial={{ width: 0 }}
                          whileInView={{ width: `${skill.level}%` }}
                          viewport={{ once: true }}
                          transition={{ duration: 1, ease: 'easeOut' }}
                          className={`h-full rounded-full bg-gradient-to-r ${skill.color}`}
                        />
                      </div>
                    </div>
                  </TiltCard>
                </motion.div>
              );
            })}
          </AnimatePresence>
        </motion.div>
      </div>
    </section>
  );
}
