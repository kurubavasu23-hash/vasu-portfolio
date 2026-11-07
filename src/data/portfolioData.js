export const personalInfo = {
  name: 'Kuruba Vasu',
  initials: 'KV',
  roles: [
    'Python Full Stack Developer',
    'Software Developer',
    'B.Tech CSE Student',
    'Django & React.js Developer',
  ],
  tagline: 'Python Full Stack Developer | Software Developer | B.Tech CSE Student',
  education: 'B.Tech Computer Science and Engineering',
  college: 'Dr. K.V. Subba Reddy Institute of Technology',
  location: 'Kurnool, Andhra Pradesh, India',
  cgpa: '8.76',
  careerGoal: 'To become a professional software developer.',
  bio: `I am a dedicated Computer Science and Engineering undergraduate at Dr. K.V. Subba Reddy Institute of Technology, Kurnool, holding a 8.76 CGPA. I specialize in architecting and building full-stack web applications using Python, Django, REST APIs, React.js, and MySQL. Passionate about clean code, scalable backend architecture, and intuitive user interfaces, my goal is to become a professional software developer solving impactful real-world engineering challenges.`,
  // Replace '/profile-placeholder.svg' with '/profile.jpg' after placing your photo in public/profile.jpg
  profilePhoto: '/profile.jpg',
  fallbackPhoto: '/profile-placeholder.svg',
  // Place your PDF in public/Kuruba_Vasu_Resume.pdf
  resumeUrl: '/Kuruba_Vasu_Resume.pdf',
  email: 'kurubavasu.dev@gmail.com',
  socials: {
    github: 'https://github.com/kurubavasu',
    linkedin: 'https://www.linkedin.com/in/kuruba-vasu',
    email: 'mailto:kurubavasu.dev@gmail.com',
  },
};

export const statsData = [
  {
    id: 1,
    label: 'B.Tech CGPA',
    value: 8.76,
    decimals: 2,
    suffix: ' / 10',
    description: 'Consistent academic excellence in CSE',
  },
  {
    id: 2,
    label: 'Featured Projects',
    value: 4,
    decimals: 0,
    suffix: '',
    description: 'Full-stack, AI & data analysis builds',
  },
  {
    id: 3,
    label: 'Technical Skills',
    value: 18,
    decimals: 0,
    suffix: '+',
    description: 'Languages, frameworks, tools & CS core',
  },
  {
    id: 4,
    label: 'Verified Certifications',
    value: 2,
    decimals: 0,
    suffix: '+',
    description: 'NPTEL AI & Ethical Hacking credentials',
  },
];

export const skillCategories = [
  'All',
  'Programming',
  'Frontend',
  'Backend',
  'Database',
  'Tools',
  'Core Subjects',
];

export const skillsData = [
  // Programming
  {
    name: 'Python',
    category: 'Programming',
    level: 92,
    badge: 'Primary Language',
    icon: 'Terminal',
    color: 'from-blue-500 to-cyan-400',
    description: 'Object-oriented programming, scripting, automation, backend web architecture, and AI integration.',
  },
  {
    name: 'JavaScript',
    category: 'Programming',
    level: 85,
    badge: 'ES6+',
    icon: 'Code2',
    color: 'from-amber-400 to-yellow-500',
    description: 'Asynchronous programming, DOM manipulation, modern ES6+ syntax, and interactive UI logic.',
  },
  {
    name: 'Java (Basics)',
    category: 'Programming',
    level: 70,
    badge: 'OOP Foundation',
    icon: 'Coffee',
    color: 'from-orange-500 to-red-500',
    description: 'Core object-oriented principles, class design, exception handling, and servlet fundamentals.',
  },

  // Frontend
  {
    name: 'HTML5',
    category: 'Frontend',
    level: 94,
    badge: 'Semantic Web',
    icon: 'Layout',
    color: 'from-orange-500 to-amber-500',
    description: 'Accessible, SEO-friendly semantic markup and modern document structure.',
  },
  {
    name: 'CSS3',
    category: 'Frontend',
    level: 90,
    badge: 'Responsive UI',
    icon: 'Palette',
    color: 'from-blue-500 to-indigo-500',
    description: 'Flexbox, CSS Grid, responsive media queries, glassmorphism, and keyframe animations.',
  },
  {
    name: 'React.js',
    category: 'Frontend',
    level: 84,
    badge: 'SPA Library',
    icon: 'Atom',
    color: 'from-cyan-400 to-blue-500',
    description: 'Component-driven architecture, React Hooks, state management, and REST API consumption.',
  },

  // Backend
  {
    name: 'Django',
    category: 'Backend',
    level: 88,
    badge: 'Python Framework',
    icon: 'Server',
    color: 'from-emerald-500 to-teal-500',
    description: 'MVT architecture, ORM modeling, authentication, admin customization, and secure backend logic.',
  },
  {
    name: 'REST APIs',
    category: 'Backend',
    level: 86,
    badge: 'API Design',
    icon: 'Webhook',
    color: 'from-violet-500 to-purple-500',
    description: 'JSON serialization, CRUD endpoints, token/session authentication, and frontend-backend integration.',
  },
  {
    name: 'Java Servlets',
    category: 'Backend',
    level: 72,
    badge: 'Server-Side Java',
    icon: 'Cpu',
    color: 'from-rose-500 to-orange-500',
    description: 'Request-response lifecycle, session management, and dynamic web application handling.',
  },

  // Database
  {
    name: 'MySQL',
    category: 'Database',
    level: 88,
    badge: 'RDBMS',
    icon: 'Database',
    color: 'from-sky-400 to-blue-600',
    description: 'Relational schema design, indexing, joins, stored queries, and Django/Python integration.',
  },
  {
    name: 'SQL',
    category: 'Database',
    level: 90,
    badge: 'Query Language',
    icon: 'Table',
    color: 'from-indigo-400 to-purple-600',
    description: 'DDL, DML, complex joins, aggregations, normalization, and data integrity constraints.',
  },

  // Tools
  {
    name: 'Git',
    category: 'Tools',
    level: 86,
    badge: 'Version Control',
    icon: 'GitBranch',
    color: 'from-orange-500 to-red-600',
    description: 'Branching workflows, commit hygiene, merge conflict resolution, and source tracking.',
  },
  {
    name: 'GitHub',
    category: 'Tools',
    level: 88,
    badge: 'Collaboration',
    icon: 'Github',
    color: 'from-slate-400 to-slate-200',
    description: 'Repository management, pull requests, project documentation, and code hosting.',
  },
  {
    name: 'VS Code',
    category: 'Tools',
    level: 92,
    badge: 'IDE',
    icon: 'Code',
    color: 'from-blue-400 to-blue-600',
    description: 'Debugging, extensions workflow, integrated terminal, and multi-language development.',
  },
  {
    name: 'Microsoft Excel',
    category: 'Tools',
    level: 85,
    badge: 'Data Analytics',
    icon: 'BarChart3',
    color: 'from-emerald-400 to-green-600',
    description: 'Pivot tables, dynamic charts, VLOOKUP/XLOOKUP, data cleaning, and interactive KPI dashboards.',
  },

  // Core Subjects
  {
    name: 'Data Structures & Algorithms',
    category: 'Core Subjects',
    level: 84,
    badge: 'Problem Solving',
    icon: 'Network',
    color: 'from-purple-500 to-pink-500',
    description: 'Arrays, linked lists, stacks, queues, trees, sorting, searching, and time-space complexity.',
  },
  {
    name: 'DBMS',
    category: 'Core Subjects',
    level: 88,
    badge: 'Core CS',
    icon: 'HardDrive',
    color: 'from-cyan-400 to-teal-500',
    description: 'ACID properties, ER modeling, relational algebra, normalization (1NF–BCNF), and transactions.',
  },
  {
    name: 'Operating Systems',
    category: 'Core Subjects',
    level: 82,
    badge: 'Core CS',
    icon: 'Layers',
    color: 'from-blue-500 to-purple-500',
    description: 'Process scheduling, multithreading, memory management, deadlocks, and file systems.',
  },
  {
    name: 'Computer Networks',
    category: 'Core Subjects',
    level: 82,
    badge: 'Core CS',
    icon: 'Globe',
    color: 'from-indigo-500 to-cyan-400',
    description: 'OSI & TCP/IP models, HTTP/HTTPS protocols, DNS, routing, and client-server communication.',
  },
];

export const projectsData = [
  {
    id: 'shopsphere',
    title: 'ShopSphere – Full Stack E-Commerce Web Application',
    category: 'Full Stack Web Application',
    shortDescription:
      'A comprehensive full-stack e-commerce web application engineered with a responsive storefront, product catalog management, shopping cart workflows, and relational database persistence.',
    architectureSummary:
      'Built using a modular full-stack architecture separating presentation components from backend business logic and relational database tables.',
    features: [
      'Dynamic product catalog with category filtering and search functionality',
      'User authentication, session management, and secure account workflows',
      'Interactive shopping cart state management and order checkout pipeline',
      'Relational database schema in MySQL managing products, users, and orders',
    ],
    technologies: ['Python', 'Django', 'React.js', 'JavaScript', 'HTML5', 'CSS3', 'MySQL', 'REST APIs'],
    githubUrl: 'https://github.com/kurubavasu',
    liveUrl: null,
    accentColor: 'from-blue-500 via-indigo-500 to-purple-600',
  },
  {
    id: 'student-placement',
    title: 'Student Placement Management System',
    category: 'Enterprise Web System',
    shortDescription:
      'A centralized academic placement portal designed to streamline student profile management, eligibility filtering, placement drive tracking, and coordinator workflows.',
    architectureSummary:
      'Role-based web application connecting students and placement coordinators through structured SQL database records and clean backend controllers.',
    features: [
      'Student registration, academic record management, and resume profile storage',
      'Automated filtering of eligible candidates based on CGPA and branch criteria',
      'Placement drive announcements and application status tracking',
      'Structured MySQL relational schema ensuring data consistency and fast queries',
    ],
    technologies: ['Python', 'Django', 'HTML5', 'CSS3', 'JavaScript', 'MySQL', 'SQL'],
    githubUrl: 'https://github.com/kurubavasu',
    liveUrl: null,
    accentColor: 'from-cyan-500 via-blue-500 to-indigo-600',
  },
  {
    id: 'call-centre-dashboard',
    title: 'Call Centre Data Analysis Dashboard using Microsoft Excel',
    category: 'Data Analytics & Visualization',
    shortDescription:
      'An interactive analytical dashboard built in Microsoft Excel to transform raw call centre records into actionable performance insights, KPI summaries, and visual trend reports.',
    architectureSummary:
      'End-to-end spreadsheet data pipeline utilizing data cleaning, Pivot Tables, dynamic slicers, and custom visualization charts.',
    features: [
      'Data cleaning, normalization, and structured formatting of call log datasets',
      'Interactive Pivot Tables and multi-dimensional slicers for dynamic filtering',
      'Visual tracking of call volume trends, resolution metrics, and agent performance',
      'Executive summary layout designed for clear operational decision-making',
    ],
    technologies: ['Microsoft Excel', 'Pivot Tables', 'Data Cleaning', 'Data Visualization', 'Dashboard Design'],
    githubUrl: 'https://github.com/kurubavasu',
    liveUrl: null,
    accentColor: 'from-emerald-500 via-teal-500 to-cyan-600',
  },
  {
    id: 'hey-vasu-ai',
    title: 'Hey Vasu – AI Voice Assistant',
    category: 'AI & Python Automation',
    shortDescription:
      'An intelligent Python-powered desktop voice assistant capable of recognizing spoken commands, synthesizing natural speech responses, and automating everyday system and web tasks.',
    architectureSummary:
      'Event-driven Python voice pipeline integrating speech-to-text recognition, command parsing, task execution modules, and text-to-speech synthesis.',
    features: [
      'Real-time voice wake-word and speech recognition command processing',
      'Natural text-to-speech audio feedback loop for conversational interaction',
      'Automated web searches, application launching, and information retrieval',
      'Modular Python command handler architecture for easy skill extensibility',
    ],
    technologies: ['Python', 'Speech Recognition', 'Text-to-Speech', 'Automation', 'APIs'],
    githubUrl: 'https://github.com/kurubavasu',
    liveUrl: null,
    accentColor: 'from-purple-500 via-fuchsia-500 to-pink-600',
  },
];

export const educationData = [
  {
    id: 'btech',
    degree: 'Bachelor of Technology (B.Tech) – Computer Science and Engineering',
    institution: 'Dr. K.V. Subba Reddy Institute of Technology',
    location: 'Kurnool, Andhra Pradesh, India',
    period: 'Pursuing (Undergraduate)',
    scoreLabel: 'CGPA',
    score: '8.76',
    highlights: [
      'Core focus on Software Engineering, Data Structures & Algorithms, DBMS, Operating Systems, and Computer Networks.',
      'Hands-on development of full-stack web applications using Python, Django, React.js, and MySQL.',
      'Active participant in technical certifications, coding labs, and software project exhibitions.',
    ],
  },
  {
    id: 'intermediate',
    degree: 'Intermediate Education (Class XII – MPC)',
    institution: 'Board of Intermediate Education, Andhra Pradesh',
    location: 'Andhra Pradesh, India',
    period: 'Completed',
    scoreLabel: 'Stream',
    score: 'Mathematics, Physics & Chemistry',
    highlights: [
      'Built strong analytical and mathematical foundations in calculus, algebra, and physical sciences.',
      'Developed logical problem-solving skills that transitioned directly into computer science fundamentals.',
    ],
  },
  {
    id: 'school',
    degree: 'Secondary School Education (SSC – Class X)',
    institution: 'Board of Secondary Education, Andhra Pradesh',
    location: 'Andhra Pradesh, India',
    period: 'Completed',
    scoreLabel: 'Foundation',
    score: 'General Sciences & Mathematics',
    highlights: [
      'Completed foundational schooling with strong academic discipline in mathematics, science, and computer literacy.',
    ],
  },
];

export const certificationsData = [
  {
    id: 'nptel-ai',
    title: 'NPTEL Fundamentals of AI',
    issuer: 'NPTEL (National Programme on Technology Enhanced Learning)',
    category: 'Artificial Intelligence',
    status: 'Verified Certification',
    skillsCovered: [
      'Intelligent Agents & Problem Solving',
      'Search Algorithms & Heuristics',
      'Knowledge Representation & Reasoning',
      'Foundations of Machine Intelligence',
    ],
    description:
      'Completed rigorous academic coursework covering the theoretical and algorithmic foundations of Artificial Intelligence through the NPTEL initiative.',
  },
  {
    id: 'ethical-hacking',
    title: 'Ethical Hacking Certification',
    issuer: 'Verified Technical Certification',
    category: 'Cybersecurity & Application Security',
    status: 'Verified Certification',
    skillsCovered: [
      'Network Security Fundamentals',
      'Web Application Vulnerability Awareness',
      'Reconnaissance & Security Assessment Concepts',
      'Defensive Coding & Secure Authentication Practices',
    ],
    description:
      'Trained in ethical hacking methodologies, system vulnerability assessment, network protocols, and secure web application development practices.',
  },
  {
    id: 'fullstack-python-cert',
    title: 'Python Full Stack & Database Development Training',
    issuer: 'Academic & Technical Skill Verification',
    category: 'Full Stack Software Engineering',
    status: 'Verified Competency',
    skillsCovered: [
      'Python Object-Oriented Programming',
      'Django Web Framework & REST APIs',
      'Relational Database Design with MySQL & SQL',
      'Frontend Development with HTML5, CSS3, JS & React.js',
    ],
    description:
      'Demonstrated practical proficiency across the full software development lifecycle through verified academic coursework and end-to-end project implementations.',
  },
];

export const experienceData = [
  {
    id: 'practical-dev',
    role: 'Full Stack Software Development (Project Engineering)',
    type: 'Practical Development Experience',
    organization: 'Self-Directed & Academic Engineering Projects',
    location: 'Kurnool, Andhra Pradesh',
    highlights: [
      'Architected and developed ShopSphere, a full-stack e-commerce web application integrating Python, Django, REST APIs, React.js, and MySQL.',
      'Engineered a Student Placement Management System with relational SQL schemas to automate candidate eligibility filtering and placement workflows.',
      'Built "Hey Vasu", a modular Python AI Voice Assistant leveraging speech recognition, text-to-speech synthesis, and task automation.',
      'Designed an interactive Call Centre Data Analysis Dashboard in Microsoft Excel utilizing Pivot Tables, dynamic slicers, and KPI visualizations.',
    ],
    technologies: ['Python', 'Django', 'React.js', 'REST APIs', 'MySQL', 'Git & GitHub', 'Microsoft Excel'],
  },
  {
    id: 'technical-training',
    role: 'Technical Training & Core Computer Science Labs',
    type: 'Technical Training',
    organization: 'Dr. K.V. Subba Reddy Institute of Technology',
    location: 'Kurnool, Andhra Pradesh',
    highlights: [
      'Completed intensive hands-on programming laboratories in Python, Java (Basics), Java Servlets, Data Structures & Algorithms, and Database Management Systems.',
      'Practiced database normalization, complex SQL joins, and backend server integration across structured semester engineering labs.',
      'Applied Git and GitHub version control workflows for source code management and technical documentation.',
    ],
    technologies: ['Python', 'Java (Basics)', 'Java Servlets', 'DSA', 'DBMS', 'SQL', 'OS & Networks'],
  },
  {
    id: 'internship-readiness',
    role: 'Software Engineering Internship & Applied Training',
    type: 'Internship & Career Readiness',
    organization: 'Academic & Industry Skill Development',
    location: 'Andhra Pradesh, India',
    highlights: [
      'Trained in Agile software development lifecycles, RESTful API design patterns, and responsive frontend development.',
      'Combined NPTEL Artificial Intelligence foundations and Ethical Hacking security principles to write cleaner, safer, and more maintainable code.',
      'Actively prepared for full-time Software Developer and Python Full Stack Engineer roles with a strong 8.76 CGPA academic track record.',
    ],
    technologies: ['Full Stack Web Dev', 'REST Architecture', 'Application Security', 'AI Fundamentals'],
  },
];
