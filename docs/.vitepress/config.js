export default {
  title: 'Hermes Agent 中文指南',
  description: '面向中文用户的 Hermes Agent 上手、选型与实战资源',
  themeConfig: {
    logo: '/logo.svg',
    nav: [
      { text: '首页', link: '/' },
      { text: '快速开始', link: '/quick-start' },
      { text: '模型与 Provider', link: '/models' },
      { text: '常见问题', link: '/known-issues' },
      { text: 'Starter 模板', link: '/starters/index' },
      { text: '示例项目', link: '/examples/index' }
    ],
    sidebar: [
      {
        text: '开始使用',
        items: [
          { text: '首页', link: '/' },
          { text: '快速开始', link: '/quick-start' },
          { text: '模型与 Provider', link: '/models' },
          { text: '常见问题', link: '/known-issues' }
        ]
      },
      {
        text: '进阶了解',
        items: [
          { text: 'Hermes vs OpenClaw', link: '/openclaw-compare' },
          { text: '多 Agent 协作', link: '/team-flow' }
        ]
      },
      {
        text: '资源库',
        items: [
          { text: 'Starter 模板（项目骨架）', link: '/starters/index' },
          { text: '示例项目（具体案例）', link: '/examples/index' }
        ]
      }
    ],
    socialLinks: [
      { icon: 'github', link: 'https://github.com/zcweah1981/awesome-hermes-agent-zh' }
    ],
    footer: {
      message: '面向中文用户的 Hermes Agent 使用指南。',
      copyright: 'Copyright © 2026 Hermes Agent 中文指南'
    }
  }
}
