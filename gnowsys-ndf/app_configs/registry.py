# This file tells dlkit where to find / import each of the different
# managers from.
MANAGER_PATHS = {

    'service': {
        'ASSESSMENT': ('osid.dlkit.services.assessment.AssessmentManager',
                       'osid.dlkit.services.assessment.AssessmentManager'),
        'ASSESSMENT_AUTHORING': ('osid.dlkit.services.assessment_authoring.AssessmentAuthoringManager',
                                 'osid.dlkit.services.assessment_authoring.AssessmentAuthoringManager'),
        'AUTHENTICATION': ('osid.dlkit.services.authentication.AuthenticationManager',
                           'osid.dlkit.services.authentication.AuthenticationManager'),
        'AUTHORIZATION': ('osid.dlkit.services.authorization.AuthorizationManager',
                          'osid.dlkit.services.authorization.AuthorizationManager'),
        'REPOSITORY': ('osid.dlkit.services.repository.RepositoryManager',
                       'osid.dlkit.services.repository.RepositoryManager'),
        'LEARNING': ('osid.dlkit.services.learning.LearningManager',
                     'osid.dlkit.services.learning.LearningManager'),
        'LOGGING': ('osid.dlkit.services.logging_.LoggingManager',
                    'osid.dlkit.services.logging_.LoggingManager'),
        'CATALOGING': ('osid.dlkit.services.cataloging.CatalogingManager',
                       'osid.dlkit.services.cataloging.CatalogingManager'),
        'COMMENTING': ('osid.dlkit.services.commenting.CommentingManager',
                       'osid.dlkit.services.commenting.CommentingManager'),
        'RESOURCE': ('osid.dlkit.services.resource.ResourceManager',
                     'osid.dlkit.services.resource.ResourceManager'),
        'GRADING': ('osid.dlkit.services.grading.GradingManager',
                    'osid.dlkit.services.grading.GradingManager'),
        'TYPE': ('osid.dlkit.services.type.TypeManager',
                 'osid.dlkit.services.type.TypeManager')
    },
    'json': {
        'ASSESSMENT': ('osid.dlkit.json_.assessment.managers.AssessmentManager',
                       'osid.dlkit.json_.assessment.managers.AssessmentProxyManager'),
        'ASSESSMENT_AUTHORING': ('osid.dlkit.json_.assessment_authoring.managers.AssessmentAuthoringManager',
                                 'osid.dlkit.json_.assessment_authoring.managers.AssessmentAuthoringProxyManager'),
        'AUTHENTICATION': ('osid.dlkit.json_.authentication.managers.AuthenticationManager',
                           'osid.dlkit.json_.authentication.managers.AuthenticationProxyManager'),
        'AUTHORIZATION': ('osid.dlkit.json_.authorization.managers.AuthorizationManager',
                          'osid.dlkit.json_.authorization.managers.AuthorizationProxyManager'),
        'REPOSITORY': ('osid.dlkit.json_.repository.managers.RepositoryManager',
                       'osid.dlkit.json_.repository.managers.RepositoryProxyManager'),
        'LEARNING': ('osid.dlkit.json_.learning.managers.LearningManager',
                     'osid.dlkit.json_.learning.managers.LearningProxyManager'),
        'LOGGING': ('osid.dlkit.json_.logging_.managers.LoggingManager',
                    'osid.dlkit.json_.logging_.managers.LoggingProxyManager'),
        'CATALOGING': ('osid.dlkit.json_.cataloging.managers.CatalogingManager',
                       'osid.dlkit.json_.cataloging.managers.CatalogingProxyManager'),
        'COMMENTING': ('osid.dlkit.json_.commenting.managers.CommentingManager',
                       'osid.dlkit.json_.commenting.managers.CommentingProxyManager'),
        'RESOURCE': ('osid.dlkit.json_.resource.managers.ResourceManager',
                     'osid.dlkit.json_.resource.managers.ResourceProxyManager'),
        'GRADING': ('osid.dlkit.json_.grading.managers.GradingManager',
                    'osid.dlkit.json_.grading.managers.GradingProxyManager')
    },
    'authz_adapter': {
        'ASSESSMENT': ('osid.dlkit.authz_adapter.assessment.managers.AssessmentManager',
                       'osid.dlkit.authz_adapter.assessment.managers.AssessmentProxyManager'),
        'ASSESSMENT_AUTHORING': ('osid.dlkit.authz_adapter.assessment_authoring.managers.AssessmentAuthoringManager',
                                 'osid.dlkit.authz_adapter.assessment_authoring.managers.AssessmentAuthoringProxyManager'),
        'AUTHORIZATION': ('osid.dlkit.authz_adapter.authorization.managers.AuthorizationManager',
                          'osid.dlkit.authz_adapter.authorization.managers.AuthorizationProxyManager'),
        'REPOSITORY': ('osid.dlkit.authz_adapter.repository.managers.RepositoryManager',
                       'osid.dlkit.authz_adapter.repository.managers.RepositoryProxyManager'),
        'LEARNING': ('osid.dlkit.authz_adapter.learning.managers.LearningManager',
                     'osid.dlkit.authz_adapter.learning.managers.LearningProxyManager'),
        'LOGGING': ('osid.dlkit.authz_adapter.logging_.managers.LoggingManager',
                    'osid.dlkit.authz_adapter.logging_.managers.LoggingProxyManager'),
        'CATALOGING': ('osid.dlkit.authz_adapter.cataloging.managers.CatalogingManager',
                       'osid.dlkit.authz_adapter.cataloging.managers.CatalogingProxyManager'),
        'COMMENTING': ('osid.dlkit.authz_adapter.commenting.managers.CommentingManager',
                       'osid.dlkit.authz_adapter.commenting.managers.CommentingProxyManager'),
        'RESOURCE': ('osid.dlkit.authz_adapter.resource.managers.ResourceManager',
                     'osid.dlkit.authz_adapter.resource.managers.ResourceProxyManager'),
        'GRADING': ('osid.dlkit.authz_adapter.grading.managers.GradingManager',
                    'osid.dlkit.authz_adapter.grading.managers.GradingProxyManager')
    },
    'handcar': {
        'LEARNING': ('osid.dlkit.handcar.learning.managers.LearningManager',
                     'osid.dlkit.handcar.learning.managers.LearningProxyManager'),
        'TYPE': ('osid.dlkit.handcar.type.managers.TypeManager',
                 'osid.dlkit.handcar.type.managers.TypeManager'),
        'REPOSITORY': ('osid.dlkit.handcar.repository.managers.RepositoryManager',
                       'osid.dlkit.handcar.repository.managers.RepositoryProxyManager'),
    },
    'aws_adapter': {
        'REPOSITORY': ('osid.dlkit.aws_adapter.repository.managers.RepositoryManager',
                       'osid.dlkit.aws_adapter.repository.managers.RepositoryProxyManager')
    },
    'filesystem_adapter': {
        'REPOSITORY': ('osid.dlkit.filesystem_adapter.repository.managers.RepositoryManager',
                       'osid.dlkit.filesystem_adapter.repository.managers.RepositoryProxyManager')
    },
    'always_authz': {
        'AUTHORIZATION': ('osid.tests.authz_impls.always_authz.AuthorizationManager',
                          'osid.tests.authz_impls.always_authz.AuthorizationProxyManager')
    },
    'never_authz': {
        'AUTHORIZATION': ('osid.tests.authz_impls.never_authz.AuthorizationManager',
                          'osid.tests.authz_impls.never_authz.AuthorizationProxyManager')
    },

}