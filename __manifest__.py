{
    'name': '360 Feedbacks',
    'version': '1.0',
    'category': 'Feedbacks',
    'summary': 'Custom Module Feedbacks',
    'description': """
        Custom module for mini project dagangan
    """,
    'website': 'Website',
    'author': 'Eclisse',
    'depends': ['base'],
    'data': [
            'data/sequence.xml',
            'views/feedbacks_roles_view.xml',
            'views/feedbacks_roles_action.xml',
            'views/feedbacks_persons_view.xml',
            'views/feedbacks_persons_action.xml',
            'views/feedbacks_question_view.xml',
            'views/feedbacks_question_action.xml',
            'views/feedbacks_questionnaire_view.xml',
            'views/feedbacks_questionnaire_action.xml',
            'views/feedbacks_answer_view.xml',
            'views/feedbacks_answer_action.xml',
            'views/feedbacks_menuitem.xml',
            'security/ir.model.access.csv'
        ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OEEL-1',
}