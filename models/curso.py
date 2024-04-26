from odoo import models, fields, api


class Profesor(models.Model):
    _name = 'gestor.profesor'
    _description = 'Modelo para representar los datos del docentes'
    
    name = fields.Char(string='Nombre', required=True)
    lastname = fields.Char(string='Apellido', required=True)
    no_identif = fields.Char(string='Número de Identificación', required=True)
    estatus = fields.Selection([('activo', 'Activo'), ('inactivo', 'Inactivo')], string='Estatus', required=True, default='activo')
    pnf = fields.Many2one('gestor.pnf', string='PNF', required=True)


class Estudiante(models.Model):
    _name = 'gestor.estudiante'
    _description = 'Modelo para representar los datos de los estudiantes'

    name = fields.Char(string='Nombre', required=True)
    lastname = fields.Char(string='Apellido', required=True)
    no_identif = fields.Char(string='Número de Identificación', required=True)
    estatus = fields.Selection([('activo', 'Activo'), ('inactivo', 'Inactivo')], string='Estatus', required=True, default='activo')
    pnf = fields.Many2one('gestor.pnf', string='PNF', required=True)
    semestre = fields.Many2one('gestor.semestre', string='Semestre', required=True)


class Pnf(models.Model):
    _name = 'gestor.pnf'
    _description = 'Modelo para representar los pnf'
    
    name = fields.Char(string='pnf', required=True)


class Trayecto(models.Model):
    _name = 'gestor.trayecto'
    _description = 'Modelo para representar los trayectos'
     
    numero = fields.Integer(string='Número de Trayecto', required=True)


class Semestre(models.Model):
    _name = 'gestor.semestre'
    _description = 'Modelo para representar los semestres de la carrera'

    numero = fields.Integer(string='Número de Semestre', required=True)
    trayecto_id = fields.Many2one('gestor.trayecto', string='Trayecto', required=True)


class Nucleo(models.Model):
    _name = 'gestor.nucleo'
    _description = 'Modelo para representar los nucleos'
     
    name = fields.Char(string='nucleo', required=True)
    codigo = fields.Char(string='Código del Núcleo', required=True)
    ubicacion = fields.Integer(string='Unidad Curricular', required=True)
    pnf = fields.Many2one('gestor.pnf', string='PNF', required=True)
    aulas_ids = fields.One2many('gestor.aula','nucleo',string='Aulas')


class Periodo(models.Model):
    _name = 'gestor.periodo'
    _description = 'Modelo para representar los periodos académicos'

    name = fields.Char(string='Nombre del Periodo', required=True)
    fecha_inicio = fields.Date(string='Fecha de Inicio', required=True)
    fecha_fin = fields.Date(string='Fecha de Fin', required=True)


class UnidadCurricular(models.Model):
    _name = 'gestor.unidad_curricular'
    _description = 'Modelo para representar las unidades curriculares'
     
    name = fields.Char(string='Unidad curricular', required=True)
    unidad_de_credito = fields.Integer(string='Unidad Curricular', required=True)
    pnf = fields.Many2one('gestor.pnf', string='PNF', required=True)


class Aula(models.Model):
    _name = 'gestor.aula'
    _description = 'Modelo para representar las aulas'

    name = fields.Char(string='Nombre del Aula', required=True)
    capacidad = fields.Integer(string='Capacidad', required=True)
    edificio = fields.Char(string='Edificio', required=True)
    piso = fields.Integer(string='Piso', required=True)
    nucleo = fields.Many2one('gestor.nucleo', string='Nucleo', required=True)


class Modalidad(models.Model):
    _name = 'gestor.modalidad'
    _description = 'Modelo para representar la modalidad'

    modalidad = fields.Selection([('Presencial', 'Presencial'), ('Virtual', 'Virtual')], string='Modalidad', required=True)


class Turno(models.Model):
    _name = 'gestor.turno'
    _description = 'Modelo para representar los turnos académicos'

    name = fields.Char(string='Nombre del Turno', required=True)
    descripcion = fields.Selection([
        ('Diurno', 'Diurno'), 
        ('Vespertino', 'Vespertino'),
        ('Nocturno', 'Nocturno'),
        ('Diurno-Nocturno', 'Diurno-Nocturno'),
        ('Diurno-Vespertino', 'Diurno-Vespertino'),
        ('Vespertino-Nocturno', 'Vespertino-Nocturno'),
        ('TurnoCompleto', 'TurnoCompleto')
    ], string='Turno', required=True)


class Dia(models.Model):
    _name = 'gestor.dia'
    _description = 'Modelo para representar los días de la semana'

    name = fields.Selection(
        [
            ('Lunes', 'Lunes'), 
            ('Martes', 'Martes'), 
            ('Miércoles', 'Miércoles'), 
            ('Jueves', 'Jueves'), 
            ('Viernes', 'Viernes')
        ], string='Nombre del Día', required=True
    )


class DiasConHoras(models.Model):
    _name = 'gestor.dias_con_horas'
    _description = 'Modelo para representar los días de la semana'

    hora_inicio = fields.Datetime(string='Hora de Inicio', required=True)
    hora_fin = fields.Datetime(string='Hora de Fin', required=True)
    dia_ids = fields.Many2one('gestor.dia', string='Días', required=True)
    turno_id = fields.Many2one('gestor.turno', string='Turno')
    aula_id = fields.Many2one('gestor.aula', string='Aula', required=True)


class Curso(models.Model):
    _name = 'gestor.curso'
    _description = 'Modelo para representar los cursos de las clases'

    dias_con_horas_ids = fields.Many2many('gestor.dias_con_horas', string='DiasConHoras', required=True)
    profesor_id = fields.Many2one('gestor.profesor', string='Profesor', required=True)
    unidad_curricular_id = fields.Many2one('gestor.unidad_curricular', string='Unidad Curricular', required=True)
    periodo_id = fields.Many2one('gestor.periodo', string='Periodo', required=True)
    modalidad = fields.Many2one('gestor.modalidad', string='Modalidad', required=True)
    semestre = fields.Many2one('gestor.semestre', string='Semestre', required=True)


class ClaseInscrita(models.Model):
    _name = 'gestor.clase_inscrita'
    _description = 'Modelo para representar las clases inscritas por los estudiantes'

    estudiante_id = fields.Many2one('gestor.estudiante', string='Estudiante', required=True)
    curso_id = fields.Many2one('gestor.curso', string='Horario de la Clase', required=True)

    estudiante_identif = fields.Char(string='Identificación del Estudiante', compute='_compute_estudiante_identif')
    estudiante_name = fields.Char(string='Nombre del Estudiante', compute='_compute_estudiante_name')
    profesor_identif = fields.Char(string='Identificación del Profesor', compute='_compute_profesor_identif')
    profesor_name = fields.Char(string='Nombre del Profesor', compute='_compute_profesor_name')
    unidad_curricular_name = fields.Char(string='Nombre de la Unidad Curricular', compute='_compute_unidad_curricular_name')
    modalidad = fields.Char(string='Modalidad', compute='_compute_modalidad')
    periodo = fields.Char(string='Periodo', compute='_compute_periodo')
    hora_inicio = fields.Datetime(string='Hora de Inicio', compute='_compute_hora_inicio')
    hora_fin = fields.Datetime(string='Hora de Fin', compute='_compute_hora_fin')
    dia = fields.Char(string='Día', compute='_compute_dia')
    turno = fields.Char(string='Turno', compute='_compute_turno')
    aula = fields.Char(string='Aula', compute='_compute_aula')
    nucleo = fields.Char(string='Nucleo', compute='_compute_nucleo')
    pnf = fields.Char(string='Pnf', compute='_compute_pnf')
    trayecto = fields.Char(string='Trayecto', compute='_compute_trayecto')
    semestre = fields.Char(string='Semestre', compute='_compute_semestre')

    @api.depends('estudiante_id.no_identif')
    def _compute_estudiante_identif(self):
        for record in self:
            record.estudiante_identif = record.estudiante_id.no_identif

    @api.depends('estudiante_id.name')
    def _compute_estudiante_name(self):
        for record in self:
            record.estudiante_name = record.estudiante_id.name

    @api.depends('curso_id.profesor_id.no_identif')
    def _compute_profesor_identif(self):
        for record in self:
            record.profesor_identif = record.curso_id.profesor_id.no_identif

    @api.depends('curso_id.profesor_id.name')
    def _compute_profesor_name(self):
        for record in self:
            record.profesor_name = record.curso_id.profesor_id.name

    @api.depends('curso_id.unidad_curricular_id.name')
    def _compute_unidad_curricular_name(self):
        for record in self:
            record.unidad_curricular_name = record.curso_id.unidad_curricular_id.name

    @api.depends('curso_id.modalidad.modalidad')
    def _compute_modalidad(self):
        for record in self:
            record.modalidad = record.curso_id.modalidad.modalidad

    @api.depends('curso_id.periodo_id.name')
    def _compute_periodo(self):
        for record in self:
            record.periodo = record.curso_id.periodo_id.name

    @api.depends('curso_id.dias_con_horas_ids.hora_inicio')
    def _compute_hora_inicio(self):
        for record in self:
            record.hora_inicio = record.curso_id.dias_con_horas_ids.hora_inicio

    @api.depends('curso_id.dias_con_horas_ids.hora_fin')
    def _compute_hora_fin(self):
        for record in self:
            record.hora_fin = record.curso_id.dias_con_horas_ids.hora_fin

    @api.depends('curso_id.dias_con_horas_ids.dia_ids.name')
    def _compute_dia(self):
        for record in self:
            record.dia = ', '.join([dia.name for dia in record.curso_id.dias_con_horas_ids.dia_ids])

    @api.depends('curso_id.dias_con_horas_ids.turno_id.name')
    def _compute_turno(self):
        for record in self:
            record.turno = record.curso_id.dias_con_horas_ids.turno_id.name

    @api.depends('curso_id.dias_con_horas_ids.aula_id.name')
    def _compute_aula(self):
        for record in self:
            record.aula = record.curso_id.dias_con_horas_ids.aula_id.name

    @api.depends('curso_id.dias_con_horas_ids.aula_id.nucleo.name')
    def _compute_nucleo(self):
        for record in self:
            record.nucleo = record.curso_id.dias_con_horas_ids.aula_id.nucleo.name

    @api.depends('curso_id.unidad_curricular_id.pnf.name')
    def _compute_pnf(self):
        for record in self:
            record.pnf = record.curso_id.unidad_curricular_id.pnf.name

    @api.depends('curso_id.semestre.trayecto_id.numero')
    def _compute_trayecto(self):
        for record in self:
            record.trayecto = record.curso_id.semestre.trayecto_id.numero

    @api.depends('curso_id.semestre.numero')
    def _compute_semestre(self):
        for record in self:
            record.semestre = record.curso_id.semestre.numero

