import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Award, ShieldCheck, CheckCircle2, Sparkles, X } from 'lucide-react';
import { certificationsData } from '../data/portfolioData';
import SectionHeading from './SectionHeading';
import TiltCard from './TiltCard';

export default function Certifications() {
  const [selectedCert, setSelectedCert] = useState(null);

  return (
    <section id="certifications" className="py-20 sm:py-28 relative">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <SectionHeading
          badge="05. CREDENTIALS"
          title="Verified"
          highlight="Certifications"
          subtitle="Continuous learning validated through NPTEL Artificial Intelligence coursework, Ethical Hacking certification, and full-stack technical training."
        />

        <div className="grid grid-cols-1 md:grid-cols-3 gap-7">
          {certificationsData.map((cert, index) => (
            <motion.div
              key={cert.id}
              initial={{ opacity: 0, y: 24 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, amount: 0.25 }}
              transition={{ duration: 0.45, delay: index * 0.1 }}
            >
              <TiltCard className="glass-card rounded-3xl p-7 h-full flex flex-col justify-between group border border-slate-200/80 dark:border-white/10 hover:border-purple-500/40 transition-all">
                <div>
                  <div className="flex items-center justify-between gap-2 mb-5">
                    <div className="p-3.5 rounded-2xl bg-gradient-to-br from-blue-600 via-indigo-600 to-purple-600 text-white shadow-lg shadow-blue-500/20 group-hover:scale-110 transition-transform">
                      <Award className="w-6 h-6" />
                    </div>
                    <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/25 text-emerald-600 dark:text-emerald-400 text-xs font-mono font-semibold">
                      <ShieldCheck className="w-3.5 h-3.5" />
                      {cert.status}
                    </span>
                  </div>

                  <span className="text-xs font-mono uppercase tracking-wider text-blue-600 dark:text-blue-400 font-semibold">
                    {cert.category}
                  </span>
                  <h3 className="font-display text-xl font-bold text-slate-900 dark:text-white mt-1 mb-2">
                    {cert.title}
                  </h3>
                  <p className="text-xs font-medium text-purple-600 dark:text-purple-400 mb-4">
                    Issued by: {cert.issuer}
                  </p>
                  <p className="text-sm text-slate-600 dark:text-slate-300 leading-relaxed mb-5">
                    {cert.description}
                  </p>
                </div>

                <div>
                  <div className="space-y-1.5 mb-6 pt-4 border-t border-slate-200/70 dark:border-white/10">
                    {cert.skillsCovered.slice(0, 3).map((skill, idx) => (
                      <div
                        key={idx}
                        className="flex items-center gap-2 text-xs text-slate-600 dark:text-slate-300"
                      >
                        <CheckCircle2 className="w-3.5 h-3.5 text-blue-500 shrink-0" />
                        <span>{skill}</span>
                      </div>
                    ))}
                  </div>

                  <button
                    onClick={() => setSelectedCert(cert)}
                    className="w-full py-2.5 px-4 rounded-xl glass-pill text-xs font-semibold text-slate-800 dark:text-white hover:bg-blue-600 hover:text-white dark:hover:bg-blue-600 transition-colors flex items-center justify-center gap-2"
                  >
                    <Sparkles className="w-4 h-4" />
                    <span>View Credential Details</span>
                  </button>
                </div>
              </TiltCard>
            </motion.div>
          ))}
        </div>
      </div>

      <AnimatePresence>
        {selectedCert && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={() => setSelectedCert(null)}
            className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/75 backdrop-blur-md"
          >
            <motion.div
              initial={{ scale: 0.92, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              exit={{ scale: 0.92, opacity: 0 }}
              onClick={(e) => e.stopPropagation()}
              className="glass-card rounded-3xl max-w-lg w-full p-6 sm:p-8 border border-white/20"
            >
              <div className="flex items-start justify-between gap-4 mb-5">
                <div className="flex items-center gap-3">
                  <div className="p-3 rounded-2xl bg-gradient-to-br from-blue-600 to-purple-600 text-white">
                    <Award className="w-6 h-6" />
                  </div>
                  <div>
                    <span className="text-xs font-mono text-emerald-400 font-semibold">
                      {selectedCert.status}
                    </span>
                    <h3 className="font-display text-xl font-bold text-slate-900 dark:text-white">
                      {selectedCert.title}
                    </h3>
                  </div>
                </div>
                <button
                  onClick={() => setSelectedCert(null)}
                  className="p-2 rounded-xl glass-pill text-slate-500 hover:text-white"
                >
                  <X className="w-5 h-5" />
                </button>
              </div>

              <p className="text-xs font-mono text-blue-500 mb-3">
                Issuer: {selectedCert.issuer}
              </p>
              <p className="text-sm text-slate-600 dark:text-slate-300 leading-relaxed mb-5">
                {selectedCert.description}
              </p>

              <h4 className="text-xs font-mono uppercase tracking-wider text-purple-500 font-semibold mb-3">
                Competencies & Topics Covered
              </h4>
              <ul className="space-y-2 mb-6">
                {selectedCert.skillsCovered.map((s, i) => (
                  <li
                    key={i}
                    className="flex items-center gap-2.5 text-sm text-slate-700 dark:text-slate-200"
                  >
                    <CheckCircle2 className="w-4 h-4 text-emerald-500 shrink-0" />
                    <span>{s}</span>
                  </li>
                ))}
              </ul>

              <button
                onClick={() => setSelectedCert(null)}
                className="w-full btn-primary py-2.5 text-sm"
              >
                Close Details
              </button>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </section>
  );
}
