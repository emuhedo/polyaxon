from event_manager import event_actions, event_subjects
from event_manager.event import Attribute, Event

JOB_STARTED = '{}.{}'.format(event_subjects.JOB, event_actions.STARTED)
JOB_STARTED_TRIGGERED = '{}.{}.{}'.format(event_subjects.JOB,
                                          event_actions.STARTED,
                                          event_subjects.TRIGGER)
JOB_STOPPED = '{}.{}'.format(event_subjects.JOB, event_actions.STOPPED)
JOB_STOPPED_TRIGGERED = '{}.{}.{}'.format(event_subjects.JOB,
                                          event_actions.STOPPED,
                                          event_subjects.TRIGGER)
JOB_CREATED = '{}.{}'.format(event_subjects.JOB, event_actions.CREATED)
JOB_VIEWED = '{}.{}'.format(event_subjects.JOB, event_actions.VIEWED)
JOB_UPDATED = '{}.{}'.format(event_subjects.JOB, event_actions.UPDATED)
JOB_NEW_STATUS = '{}.{}'.format(event_subjects.JOB, event_actions.NEW_STATUS)
JOB_FAILED = '{}.{}'.format(event_subjects.JOB, event_actions.FAILED)
JOB_SUCCEEDED = '{}.{}'.format(event_subjects.JOB, event_actions.SUCCEEDED)

JOB_DELETED = '{}.{}'.format(event_subjects.JOB, event_actions.DELETED)
JOB_DELETED_TRIGGERED = '{}.{}.{}'.format(event_subjects.JOB,
                                          event_actions.DELETED,
                                          event_subjects.TRIGGER)


class JobCreatedEvent(Event):
    event_type = JOB_CREATED
    actor_id = 'user.id'
    attributes = (
        Attribute('id'),
        Attribute('project.id'),
        Attribute('project.user.id'),
        Attribute('user.id'),
        Attribute('created_at', is_datetime=True),
        Attribute('has_description', attr_type=bool),
    )


class JobUpdatedEvent(Event):
    event_type = JOB_UPDATED
    actor_id = 'user.id'
    attributes = (
        Attribute('id'),
        Attribute('project.id'),
        Attribute('project.user.id'),
        Attribute('user.id'),
        Attribute('created_at', is_datetime=True),
        Attribute('has_description', attr_type=bool),
    )


class JobStartedEvent(Event):
    event_type = JOB_STARTED
    attributes = (
        Attribute('id'),
        Attribute('user.id'),
        Attribute('project.id'),
        Attribute('project.user.id'),
        Attribute('target'),  # project, experiment_group, experiment
    )


class JobStartedTriggeredEvent(Event):
    event_type = JOB_STARTED_TRIGGERED
    actor_id = 'actor_id'
    attributes = (
        Attribute('id'),
        Attribute('user.id'),
        Attribute('project.id'),
        Attribute('project.user.id'),
        Attribute('target'),  # project, experiment_group, experiment
        Attribute('actor_id'),
    )


class JobSoppedEvent(Event):
    event_type = JOB_STOPPED
    attributes = (
        Attribute('id'),
        Attribute('user.id'),
        Attribute('project.id'),
        Attribute('project.user.id'),
        Attribute('target'),  # project, experiment_group, experiment
        Attribute('last_status'),
        Attribute('previous_status', is_required=False),
    )


class JobSoppedTriggeredEvent(Event):
    event_type = JOB_STOPPED_TRIGGERED
    actor_id = 'actor_id'
    attributes = (
        Attribute('id'),
        Attribute('user.id'),
        Attribute('project.id'),
        Attribute('project.user.id'),
        Attribute('target'),  # project, experiment_group, experiment
        Attribute('actor_id'),
        Attribute('last_status'),
    )


class JobViewedEvent(Event):
    event_type = JOB_VIEWED
    actor_id = 'actor_id'
    attributes = (
        Attribute('id'),
        Attribute('user.id'),
        Attribute('project.id'),
        Attribute('project.user.id'),
        Attribute('actor_id'),
        Attribute('last_status'),
        Attribute('target'),  # project, experiment_group, experiment
    )


class JobNewStatusEvent(Event):
    event_type = JOB_NEW_STATUS
    attributes = (
        Attribute('id'),
        Attribute('user.id'),
        Attribute('project.id'),
        Attribute('last_status'),
        Attribute('target'),  # project, experiment_group, experiment
    )


class JobSucceededEvent(Event):
    event_type = JOB_SUCCEEDED
    attributes = (
        Attribute('id'),
        Attribute('user.id'),
        Attribute('project.id'),
        Attribute('last_status'),
        Attribute('previous_status', is_required=False),
        Attribute('target'),  # project, experiment_group, experiment
    )


class JobFailedEvent(Event):
    event_type = JOB_FAILED
    attributes = (
        Attribute('id'),
        Attribute('user.id'),
        Attribute('project.id'),
        Attribute('last_status'),
        Attribute('previous_status', is_required=False),
        Attribute('target'),  # project, experiment_group, experiment
    )


class JobDeletedEvent(Event):
    event_type = JOB_DELETED
    attributes = (
        Attribute('id'),
    )


class JobDeletedTriggeredEvent(Event):
    event_type = JOB_DELETED_TRIGGERED
    actor_id = 'actor_id'
    attributes = (
        Attribute('id'),
        Attribute('user.id'),
        Attribute('project.id'),
        Attribute('project.user.id'),
        Attribute('target'),  # project, experiment_group, experiment
        Attribute('actor_id'),
    )
