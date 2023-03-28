from odoo import models, fields, api
import logging
import pdb

logger = logging.getLogger(__name__)

class FeedbackPersons(models.Model):
    _name = 'feedbacks.persons'
    _rec_name = 'personId'

    personId = fields.Char(string="Person ID", readonly=True, required=True, copy=False, index=True,
                           default='New')
    firstName = fields.Char(string="First Name")
    lastName = fields.Char(string="Last Name")
    roleId = fields.Many2one('feedbacks.roles', 'Roles')

    personListAnswer = fields.One2many('feedbacks.persons', 'personId', string="Questionaire List Answers")

    @api.model
    def create(self, vals):
        if vals.get('personId', 'New' == 'New'):
            vals['personId'] = self.env['ir.sequence'].next_by_code('self.service.person') or 'New'
        result = super(FeedbackPersons, self).create(vals)
        return result


class FeedbackQuestions(models.Model):
    _name = 'feedbacks.questions'
    _rec_name = 'questionText'

    questionId = fields.Char(string="Question ID", readonly=True, required=True, copy=False, index=True, default='New')
    questionText = fields.Char(string="Question Text")

    questionListQuestionnaire = fields.One2many('feedbacks.questionnaire', 'questionId',
                                                string="Question List Questionnaire")

    @api.model
    def create(self, vals):
        if vals.get('questionId', 'New' == 'New'):
            vals['questionId'] = self.env['ir.sequence'].next_by_code('self.service.question') or 'New'
        result = super(FeedbackQuestions, self).create(vals)
        return result


class FeedbackRoles(models.Model):
    _name = 'feedbacks.roles'
    _rec_name = 'roleName'

    roleId = fields.Char(string="Roles ID", readonly=True, required=True, copy=False, index=True,
                         default='New')
    roleName = fields.Selection([('subordinate', 'Subordinate'), ('leader', 'Leader'), ('user', 'User')],
                                string="Role Name")

    roleListPerson = fields.One2many('feedbacks.persons', 'roleId', string="Role List Person")

    roleListQuestionnaire = fields.One2many('feedbacks.questionnaire', 'roleId', string="Role List Questionnaire")

    @api.model
    def create(self, vals):
        if vals.get('roleId', 'New' == 'New'):
            vals['roleId'] = self.env['ir.sequence'].next_by_code('self.service.role') or 'New'
        result = super(FeedbackRoles, self).create(vals)
        return result


class FeedbackQuestionnaire(models.Model):
    _name = 'feedbacks.questionnaire'
    _rec_name = 'questionnaireId'

    questionnaireId = fields.Char(string="Questionnaire ID", readonly=True, required=True, copy=False, index=True,
                                  default='New')
    questionId = fields.Many2one('feedbacks.questions', string="Question Text")
    roleId = fields.Many2one('feedbacks.roles', string="Role Name")
    questionnaireListAnswer = fields.One2many('feedbacks.answers', 'questionnaireId',
                                              string="Questionnaire List Answers")

    list_questionnaire = {}

    @api.model
    def create(self, vals):
        if vals.get('questionnaireId', 'New' == 'New'):
            vals['questionnaireId'] = self.env['ir.sequence'].next_by_code('self.service.questionnaire') or 'New'
        result = super(FeedbackQuestionnaire, self).create(vals)
        return result

    @api.model
    def get_questionnaire_leader(self):
        resp = {}
        for it in self.env['feedbacks.questionnaire'].search([('roleId', '=', 'RO0002')]) :
            resp[it.questionnaireId] = it.questionId
        self.list_questionnaire = resp


class FeedbackAnswers(models.Model):
    _name = 'feedbacks.answers'

    answerId = fields.Char(string="Answer ID", readonly=True, required=True, copy=False, index=True, default='New')
    questionnaireId = fields.Many2one('feedbacks.questionnaire', string="Questionnaire ID")
    personId = fields.Many2one('feedbacks.persons', string="Person ID")
    answerPoint = fields.Selection(
        [('1', 'Sangat kurang'), ('2', 'Kurang'), ('3', 'Cukup'), ('4', 'Bagus'), ('5', 'Sangat bagus')],
        string='Selection')

    @api.model
    def create(self, vals):
        if vals.get('answerId', 'New' == 'New'):
            vals['answerId'] = self.env['ir.sequence'].next_by_code('self.service.answerId') or 'New'
        result = super(FeedbackAnswers, self).create(vals)
        return result
