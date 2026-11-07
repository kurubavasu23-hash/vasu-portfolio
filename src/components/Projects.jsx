import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import {
  Github,
  ExternalLink,
  Layers,
  CheckCircle2,
  X,
  Code2,
  FolderGit2,
  Eye,
} from 'lucide-react';
import { projectsData } from '../data/portfolioData';
import SectionHeading from './SectionHeading';
import TiltCard from './TiltCard';

export default function Projects() {
  const [activeProjectModal, setActiveProjectModal] = useState(null);

  return (
    <section id="projects" className="py-20 sm:py-28 relative">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <SectionHeading
          badge="03. FEATURED WORK"
          title="Software Engineering"
          highlight="Projects"
          subtitle="Real-world applications spanning full-stack web engineering, enterprise management portals, data analytics dashboards, and AI voice automation."
        />

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {projectsData.map((project, index) => (
            <motion.div
              key={project.id}
              initial={{ opacity: 0, y: 28 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, amount: 0.2 }}
              transition={{ duration: 0.5, delay: index * 0.1 }}
            >
              <TiltCard className="glass-card rounded-3xl overflow-hidden h-full flex flex-col justify-between group border border-slate-200/80 dark:border-white/10 hover:border-blue-500/40 transition-all">
                <div>
                  <div
                    className={`relative h-48 sm:h-56 w-full bg-gradient-to-br ${project.accentColor} p-6 flex flex-col justify-between overflow-hidden`}
                  >
                    <div className="absolute inset-0 bg-black/25 backdrop-blur-[1px]" />
                    <div className="absolute -right-10 -bottom-10 w-44 h-44 rounded-full bg-white/10 blur-xl group-hover:scale-125 transition-transform duration-500" />

                    <div className="relative z-10 flex items-center justify-between">
                      <span className="px-3.5 py-1.5 rounded-full bg-black/40 backdrop-blur-md text-white text-xs font-mono font-medium border border-white/15">
                        {project.category}
                      </span>
                      <div className="p-2.5 rounded-xl bg-black/40 backdrop-blur-md text-white border border-white/15">
                        <FolderGit2 className="w-5 h-5" />
                      </div>
                    </div>

                    <div className="relative z-10">
                      <h3 className="font-display text-xl sm:text-2xl font-bold text-white leading-snug drop-shadow-sm">
                        {project.title}
                      </h3>
                    </div>
                  </div>

                  <div className="p-6 sm:p-8">
                    <p className="text-slate-600 dark:text-slate-300 text-sm sm:text-base leading-relaxed mb-5">
                      {project.shortDescription}
                    </p>

                    <div className="space-y-2 mb-6">
                      {project.features.slice(0, 3).map((feature, i) => (
                        <div
                          key={i}
                          className="flex items-start gap-2.5 text-xs sm:text-sm text-slate-600 dark:text-slate-300"
                        >
                          <CheckCircle2 className="w-4 h-4 text-blue-500 shrink-0 mt-0.5" />
                          <span>{feature}</span>
                        </div>
                      ))}
                    </div>

                    <div className="flex flex-wrap gap-2 mb-6">
                      {project.technologies.map((tech) => (
                        <span
                          key={tech}
                          className="px-3 py-1 rounded-lg glass-pill text-xs font-mono font-medium text-blue-600 dark:text-blue-300"
                        >
                          {tech}
                        </span>
                      ))}
                    </div>
                  </div>
                </div>

                <div className="px-6 sm:px-8 pb-6 sm:pb-8 pt-4 border-t border-slate-200/70 dark:border-white/10 flex flex-wrap items-center gap-3">
                  <a
                    href={project.githubUrl}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="flex-1 inline-flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl text-xs sm:text-sm font-semibold text-slate-800 dark:text-white glass-pill hover:bg-slate-200/70 dark:hover:bg-white/15 transition-all"
                  >
                    <Github className="w-4 h-4" />
                    <span>GitHub Repository</span>
                  </a>

                  {project.liveUrl ? (
                    <a
                      href={project.liveUrl}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="flex-1 inline-flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl text-xs sm:text-sm font-semibold text-white bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-500 hover:to-purple-500 shadow-md shadow-blue-500/20 transition-all"
                    >
                      <ExternalLink className="w-4 h-4" />
                      <span>Live Demo</span>
                    </a>
                  ) : (
                    <button
                      onClick={() => setActiveProjectModal(project)}
                      className="flex-1 inline-flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl text-xs sm:text-sm font-semibold text-white bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-500 hover:to-purple-500 shadow-md shadow-blue-500/20 transition-all"
                    >
                      <Eye className="w-4 h-4" />
                      <span>Interactive Overview</span>
                    </button>
                  )}
                </div>
              </TiltCard>
            </motion.div>
          ))}
        </div>
      </div>

      <AnimatePresence>
        {activeProjectModal && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={() => setActiveProjectModal(null)}
            className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/75 backdrop-blur-md"
          >
            <motion.div
              initial={{ scale: 0.92, opacity: 0, y: 20 }}
              animate={{ scale: 1, opacity: 1, y: 0 }}
              exit={{ scale: 0.92, opacity: 0, y: 20 }}
              onClick={(e) => e.stopPropagation()}
              className="glass-card rounded-3xl max-w-2xl w-full overflow-hidden border border-white/20 shadow-2xl"
            >
              <div
                className={`p-6 sm:p-8 bg-gradient-to-r ${activeProjectModal.accentColor} text-white flex items-start justify-between gap-4`}
              >
                <div>
                  <span className="inline-block px-3 py-1 rounded-full bg-black/30 text-xs font-mono mb-2">
                    {activeProjectModal.category}
                  </span>
                  <h3 className="font-display text-2xl font-bold">
                    {activeProjectModal.title}
                  </h3>
                </div>
                <button
                  onClick={() => setActiveProjectModal(null)}
                  aria-label="Close Modal"
                  className="p-2 rounded-xl bg-black/30 hover:bg-black/50 text-white transition-colors"
                >
                  <X className="w-5 h-5" />
                </button>
              </div>

              <div className="p-6 sm:p-8 space-y-6 max-h-[75vh] overflow-y-auto">
                <div>
                  <h4 className="text-xs font-mono uppercase tracking-wider text-blue-500 font-semibold mb-2 flex items-center gap-1.5">
                    <Layers className="w-4 h-4" /> System Overview & Architecture
                  </h4>
                  <p className="text-sm sm:text-base text-slate-600 dark:text-slate-300 leading-relaxed mb-2">
                    {activeProjectModal.shortDescription}
                  </p>
                  <p className="text-sm text-slate-500 dark:text-slate-400 leading-relaxed">
                    {activeProjectModal.architectureSummary}
                  </p>
                </div>

                <div>
                  <h4 className="text-xs font-mono uppercase tracking-wider text-purple-500 font-semibold mb-3">
                    Key Technical Implementations
                  </h4>
                  <ul className="space-y-2.5">
                    {activeProjectModal.features.map((feat, idx) => (
                      <li
                        key={idx}
                        className="flex items-start gap-2.5 text-sm text-slate-700 dark:text-slate-200"
                      >
                        <CheckCircle2 className="w-4 h-4 text-emerald-500 shrink-0 mt-0.5" />
                        <span>{feat}</span>
                      </li>
                    ))}
                  </ul>
                </div>

                <div>
                  <h4 className="text-xs font-mono uppercase tracking-wider text-cyan-500 font-semibold mb-3 flex items-center gap-1.5">
                    <Code2 className="w-4 h-4" /> Technologies Used
                  </h4>
                  <div className="flex flex-wrap gap-2">
                    {activeProjectModal.technologies.map((tech) => (
                      <span
                        key={tech}
                        className="px-3 py-1.5 rounded-xl glass-pill text-xs font-mono font-semibold text-blue-600 dark:text-blue-300"
                      >
                        {tech}
                      </span>
                    ))}
                  </div>
                </div>

                <div className="pt-4 border-t border-slate-200 dark:border-white/10 flex flex-wrap items-center justify-end gap-3">
                  <a
                    href={activeProjectModal.githubUrl}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="btn-primary text-sm py-2.5 px-5"
                  >
                    <Github className="w-4 h-4" />
                    <span>View on GitHub</span>
                  </a>
                  <button
                    onClick={() => setActiveProjectModal(null)}
                    className="btn-secondary text-sm py-2.5 px-5"
                  >
                    Close Preview
                  </button>
                </div>
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </section>
  );
}
