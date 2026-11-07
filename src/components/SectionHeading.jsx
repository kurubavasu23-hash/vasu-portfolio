import React from 'react';
import { motion } from 'framer-motion';

export default function SectionHeading({ badge, title, highlight, subtitle }) {
  return (
    <div className="text-center max-w-3xl mx-auto mb-14 sm:mb-16">
      <motion.div
        initial={{ opacity: 0, y: 15 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, amount: 0.3 }}
        transition={{ duration: 0.45 }}
        className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full glass-pill text-xs sm:text-sm font-mono font-medium text-blue-600 dark:text-blue-400 mb-4"
      >
        <span className="w-2 h-2 rounded-full bg-gradient-to-r from-blue-500 to-purple-500 animate-pulse" />
        <span>{badge}</span>
      </motion.div>

      <motion.h2
        initial={{ opacity: 0, y: 18 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, amount: 0.3 }}
        transition={{ duration: 0.5, delay: 0.08 }}
        className="font-display text-3xl sm:text-4xl lg:text-5xl font-bold tracking-tight text-slate-900 dark:text-white mb-4"
      >
        {title}{' '}
        {highlight && <span className="text-gradient">{highlight}</span>}
      </motion.h2>

      {subtitle && (
        <motion.p
          initial={{ opacity: 0, y: 18 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, amount: 0.3 }}
          transition={{ duration: 0.5, delay: 0.15 }}
          className="text-slate-600 dark:text-slate-400 text-base sm:text-lg leading-relaxed"
        >
          {subtitle}
        </motion.p>
      )}
    </div>
  );
}
