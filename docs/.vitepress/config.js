export default {
  title: 'Hermes Agent 中文指南',
  description: '面向中文用户的 Hermes Agent 上手、选型与实战资源',
  themeConfig: {
    logo: '/logo.svg',
    nav: [
      { text: '首页', link: '/' },
      { text: '快速开始', link: '/quick-start' },
      { text: '模型与 Provider', link: '/models' },
      { text: 'Starter 模板', link: '/starters/index' },
      { text: '示例项目', link: '/examples/index' },
      { text: '常见问题', link: '/known-issues' }
    ],
    sidebar: [
      {
        text: '开始使用',
        items: [
          { text: '首页', link: '/' },
          { text: '快速开始', link: '/quick-start' },
          { text: '安装前准备', link: '/install-prep' },
          { text: '模型与 Provider', link: '/models' },
          { text: '常见问题', link: '/known-issues' }
        ]
      },
      {
        text: '选型与协作',
        items: [
          { text: 'Hermes 到底适合谁，不适合谁', link: '/fit-guide' },
          { text: 'Hermes vs OpenClaw', link: '/openclaw-compare' },
          { text: '从 OpenClaw 迁移到 Hermes', link: '/openclaw-migration' },
          { text: '迁移后校验清单', link: '/migration-checklist' },
          { text: '多 Agent 协作', link: '/team-flow' },
          { text: 'SOUL 管角色，MD 管项目', link: '/soul-md-workflow' }
        ]
      },
      {
        text: '模板与结构',
        items: [
          { text: 'Starter 模板（项目骨架）', link: '/starters/index' },
          { text: 'single-agent starter 模板说明', link: '/single-agent-starter-guide' },
          { text: 'team-basic starter 模板说明', link: '/team-basic-starter-guide' },
          { text: 'Hermes 项目目录组织规范', link: '/project-structure' },
          { text: 'Hermes 项目文件编写指南', link: '/project-files-guide' },
          { text: 'Hermes 中文用户最常见的 3 条使用路径', link: '/user-paths' }
        ]
      },
      {
        text: '案例与排查',
        items: [
          { text: '示例项目（具体案例）', link: '/examples/index' },
          { text: '自定义 OpenAI-Compatible 接口配置指南', link: '/custom-openai-compatible' },
          { text: '常见配置错误排查', link: '/config-errors' },
          { text: '第一次跑不起来时的标准排查顺序', link: '/first-run-checklist' }
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
